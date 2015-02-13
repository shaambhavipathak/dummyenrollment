#   -*- coding: utf-8 -*-
"""
    dummyenrollment.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import ModelSQL, ModelView, fields
from tryton.pool import PoolMeta
from trytond.pyson import Eval

""" The above commands import all the required modules which will be used"""

__all__ = [
    'Party', 'personal_details', 'card_details', 'educational_background',
    'prior_experience', 'skill_set', 'family_details', 'medical_issues'
]
__metaclass__ = PoolMeta

STATES = {
    'readonly': ~Eval('active'),
}
DEPENDS = ['active']

""" This extension is required because we are extending the Party module
due to its limited number of classes (Name, Address and Contact Mechanism),
so, we need to define those classes which we have individually created. """


class Party:
    __name__ = 'party.party'

    personal_details = fields.One2Many(
        'party.personal_details', 'party', 'personal_details',
        states=STATES, depends=DEPENDS
    )
    educational_background = fields.One2Many(
        'party.educational_background', 'party', 'educational_background',
        states=STATES, depends=DEPENDS
    )
    prior_experience = fields.One2Many(
        'party.prior_experience', 'party', 'prior_experience',
        states=STATES, depends=DEPENDS
    )
    skill_set = fields.One2Many(
        'party.skill_set', 'party', 'skill_set', states=STATES, depends=DEPENDS
    )
    card_details = fields.One2Many(
        'party.card_details', 'party', 'card_details',
        states=STATES, depends=DEPENDS
    )
    family_details = fields.One2Many(
        'party.family_details', 'party', 'family_details',
        states=STATES, depends=DEPENDS
    )
    medical_issues = fields.One2Many(
        'party.medical_issues', 'party', 'medical_issues',
        states=STATES, depends=DEPENDS
    )


"""The class personal_details has the following fields:
date of birth, age, gender, hobbies and marital status along with the
inherited name, contact.mechanism and address fields of the party module"""


class personal_details(ModelSQL, ModelView):
    __name__ = "party.party"

    date_birth = fields.Date(
        'Date of Birth', required=True, states=STATES, depends=DEPENDS
    )
    birth_place = fields.Char(
        'Place of Birth', required=True, states=STATES, depends=DEPENDS
    )
    age = fields.Numeric(
        'Age', required=True, states=STATES, depends=DEPENDS
    )
    gender = fields.Selection([
        ('Male', 'M'),
        ('Female', 'F'),
        ('UNdefined', 'N/A'),
        ], 'Gender', required=True, states=STATES, depends=DEPENDS
    )
    hobbies = fields.Text(
        'Hobbies', states=STATES, depends=DEPENDS
    )
    marital_status = fields.Selection([
        ('Yes'),
        ('No'),
        ], 'Marital Status', states=STATES, depends=DEPENDS
    )

    @staticmethod
    def default_nationality():
        return 'Indian'

""" The static method will return the default nationality as
Indian, however, the fields can be edited."""

"""The class card_details has the following fields: PAN card details,
Passport details, Aadhar card details and Driving license details.
The fields have not been marked compulsory user convenience.
So, the individual may enter only those details of which
he/she can produce document proof."""


class card_details(ModelSQL, ModelView):
    __name__ = "party.party"

    pan_details = fields.Char(
        'PAN Card Number', states=STATES, depends=DEPENDS
    )
    passport_details = fields.Char(
        'Passport Number', states=STATES, depends=DEPENDS
    )
    aadhar_details = fields.Char(
        'Aadhar Card Number', states=STATES, depends=DEPENDS
    )
    driving_licence = fields.Char(
        'Driving License Number', states=STATES, depends=DEPENDS
    )

""" The class educational_background has the following fields:
Metriculation, Intermediate, Graduation and their corresponding
details such as the institution name, place, year of passing,
percentage and specialization"""


class educational_background(ModelSQL, ModelView):
    __name__ = "party.educational_background"
    party = fields.Many2One(
        'party.party', 'Party', required=True
    )
    highschool = fields.Char(
        'Metriculation', required=True
    )
    year = fields. Numeric(
        'Year', required=True
    )
    percentage = fields.Numeric(
        'Percentage', required=True
    )
    schooldetails = fields.Char(
        'School name', required=True
    )
    city = fields.Char(
        'City', required=True
    )
    seniorsecondary = fields.Char(
        'Intermediate', required=True
    )
    year = fields. Numeric(
        'Year', required=True
    )
    percentage = fields.Numeric(
        'Percentage', required=True
    )
    schooldetails = fields.Char(
        'School name', required=True
    )
    city = fields.Char(
        'City', required=True
    )
    graduation = fields.Char(
        'Graduation branch', required=True
    )
    specialization = fields.Char(
        'Specialization', required=True
    )
    year = fields. Numeric(
        'Year', required=True
    )
    percentage = fields.Numeric(
        'Percentage/CGPA', required=True
    )
    universitydetails = fields.Char(
        'University name', required=True
    )
    city = fields.Char(
        'City', required=True
    )

"""The class prior_experience is for experienced employees.
It has the following fields: firm name, city, posiiton held, tenure, reasons
for leaving the company, references and their contact details """


class prior_experience(ModelSQL, ModelView):
    __name__ = 'party.prior_experience'
    party = fields.Many2One(
        'party.party', 'Party', required=True
    )
    firm = fields.Char(
        'Name of Company'
    )
    city = fields.Char(
        'City'
    )
    post_held = fields.Char(
        'Position Held'
    )
    yearsofexperience = fields.Numeric(
        'Tenure'
    )
    reason = fields.text(
        'Reason for leaving the company'
    )
    references = fields.Char(
        'Reference'
    )
    reference_contact = fields.Numeric(
        'Contact'
    )
    reference_email = fields.Char(
        'Email ID'
    )

"""The skill_set enlists the skills an employee has. It has
the following fields: Skills, Certification/Courses and
Description of the project(s) undertaken"""


class skill_set(ModelSQL, ModelView):
    __name__ = 'party.skill_set'
    party = fields.Many2One(
        'party.party', 'Party', reuqired=True,
    )
    skill_area = fields.Char(
        'Skills'
    )
    certification = fields.Char(
        'Certification/Courses undertaken'
    )
    description = fields.Text(
        'Describe your project underake during certification'
    )

"""The family_details has the details of the family background
of the employee. It has the following fields: Father's name,
Occupation, Mother's name, Mother's occupation
and parents' contact details. """


class family_details(ModelSQL, ModelView):
    __name__ = 'party.family_details'

    name_father = fields.Char(
        "Father's name", required=True, states=STATES, depends=DEPENDS
    )
    father_occupation = fields.Char(
        "Father's occupation", states=STATES, depends=DEPENDS
    )
    nameofmother = fields.Char(
        "Mother's Name", required=True, states=STATES, depends=DEPENDS
    )
    mother_occupation = fields.Char(
        "Mother's occupation", states=STATES, depends=DEPENDS
    )
    parent_contact = fields.Many2One(
        "party.contact_mechanism", "Contact Details",
        states=STATES, depends=DEPENDS
    )

"""The medical_issues are useful incase of any emergency.
It has the following fields: Blood Group, Famliy Doctor,
Allergies, Disease History (both past and current
ailments and medications being undertaken. """


class medical_issues(ModelSQL, ModelView):
    blood_group = fields.Char(
        "Blood Group", size=5, states=STATES, depends=DEPENDS
    )
    family_doctor = fields.Char(
        "Doctor's name", states=STATES, depends=DEPENDS
    )
    doctor_contact = fields.Many2One(
        "party.contact_mechanism", "Doctor's Contact", states=STATES,
        depends=DEPENDS
    )
    allergies = fields.Text(
        "Allergies", states=STATES, depends=DEPENDS
    )
    diseasehistory = fields.Char(
        "Past Diseases (if any)", states=STATES, depends=DEPENDS
    )
    currenthistory = fields.Char(
        "Current Illness (if any)", states=STATES, depends=DEPENDS
    )
    medications = fields.Char(
        "Medications being taken (if any)", states=STATES, depends=DEPENDS
    )
