from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from koalixcrm.database import Base

# Constants (Inline for now, or import if ported)
PURPOSESADDRESSINCUSTOMER = [
    ('O', 'Office'),
    ('P', 'Private'),
    ('M', 'Mobile'),
    ('F', 'Fax'),
    ('H', 'Home'),
    ('B', 'Business'),
]

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    is_staff = Column(Boolean, default=False)

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    date_of_creation = Column(DateTime(timezone=True), server_default=func.now())
    last_modification = Column(DateTime(timezone=True), onupdate=func.now())
    last_modified_by_id = Column(Integer, ForeignKey('users.id'))
    
    last_modified_by = relationship("User")
    
    # Relationships
    postal_addresses = relationship("PostalAddressForContact", back_populates="person")
    phone_addresses = relationship("PhoneAddressForContact", back_populates="person")
    email_addresses = relationship("EmailAddressForContact", back_populates="person")
    
    type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'contact',
        'polymorphic_on': type
    }

class Customer(Contact):
    __tablename__ = 'customers'
    id = Column(Integer, ForeignKey('contacts.id'), primary_key=True)
    is_lead = Column(Boolean, default=True)
    
    # default_billing_cycle_id = Column(Integer, ForeignKey('billing_cycles.id')) # TODO: Port BillingCycle
    
    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

class PostalAddress(Base):
    __tablename__ = 'postal_addresses'
    id = Column(Integer, primary_key=True)
    prefix = Column(String(1))
    name = Column(String(100))
    pre_name = Column(String(100))
    address_line_1 = Column(String(200))
    address_line_2 = Column(String(200))
    address_line_3 = Column(String(200))
    address_line_4 = Column(String(200))
    zip_code = Column(Integer)
    town = Column(String(100))
    state = Column(String(100))
    country = Column(String(2))
    
    type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'postal_address',
        'polymorphic_on': type
    }

class PostalAddressForContact(PostalAddress):
    __tablename__ = 'postal_addresses_contact'
    id = Column(Integer, ForeignKey('postal_addresses.id'), primary_key=True)
    purpose = Column(String(1))
    person_id = Column(Integer, ForeignKey('contacts.id'))
    
    person = relationship("Contact", back_populates="postal_addresses")
    
    __mapper_args__ = {
        'polymorphic_identity': 'contact_postal_address',
    }

class PhoneAddress(Base):
    __tablename__ = 'phone_addresses'
    id = Column(Integer, primary_key=True)
    phone = Column(String(20))
    
    type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'phone_address',
        'polymorphic_on': type
    }

class PhoneAddressForContact(PhoneAddress):
    __tablename__ = 'phone_addresses_contact'
    id = Column(Integer, ForeignKey('phone_addresses.id'), primary_key=True)
    purpose = Column(String(1))
    person_id = Column(Integer, ForeignKey('contacts.id'))
    
    person = relationship("Contact", back_populates="phone_addresses")

    __mapper_args__ = {
        'polymorphic_identity': 'contact_phone_address',
    }

class EmailAddress(Base):
    __tablename__ = 'email_addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String(200))

    type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'email_address',
        'polymorphic_on': type
    }

class EmailAddressForContact(EmailAddress):
    __tablename__ = 'email_addresses_contact'
    id = Column(Integer, ForeignKey('email_addresses.id'), primary_key=True)
    purpose = Column(String(1))
    person_id = Column(Integer, ForeignKey('contacts.id'))
    
    person = relationship("Contact", back_populates="email_addresses")

    __mapper_args__ = {
        'polymorphic_identity': 'contact_email_address',
    }
