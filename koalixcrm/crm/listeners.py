import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

logger = logging.getLogger(__name__)

def log_db_event(sender, instance, created=False, deleted=False):
    """
    Log database events (create, update, delete) for a given model instance.
    """
    event_type = "updated"
    if created:
        event_type = "created"
    elif deleted:
        event_type = "deleted"

    # Convert model instance to dictionary to log its state
    # We exclude potentially sensitive or very large fields if necessary
    try:
        instance_dict = model_to_dict(instance)
    except Exception:
        # If model_to_dict fails, fallback to a simpler representation
        instance_dict = {"id": instance.pk, "details": "unserializable"}


    log_message = (
        f"A document of type {sender.__name__} was {event_type}. "
        f"Instance ID: {instance.pk}. "
    )
    
    # In a production system, you might want to be more selective
    # about what you log to avoid leaking sensitive data.
    if not deleted:
       log_message += f"Current state: {instance_dict}"


    # Log at INFO level for NIS2 compliance
    logger.info(log_message)


def register_log_signal_for_model(model):
    """
    Dynamically connect post_save and post_delete signals for a given model.
    """
    
    # Create unique receiver functions for each model to avoid conflicts
    @receiver(post_save, sender=model, weak=False)
    def specific_post_save(sender, instance, created, **kwargs):
        log_db_event(sender, instance, created=created)

    @receiver(post_delete, sender=model, weak=False)
    def specific_post_delete(sender, instance, **kwargs):
        log_db_event(sender, instance, deleted=True)

    # Keep a reference to the receiver functions to prevent garbage collection
    # This is a simple way to manage dynamic signal receivers
    if not hasattr(register_log_signal_for_model, 'receivers'):
        register_log_signal_for_model.receivers = []
    
    register_log_signal_for_model.receivers.append(specific_post_save)
    register_log_signal_for_model.receivers.append(specific_post_delete)

    logger.debug(f"Registered NIS2 logging signals for model {model.__name__}")
