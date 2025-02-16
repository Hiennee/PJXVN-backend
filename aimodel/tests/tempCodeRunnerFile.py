import pytest
from aimodel.models.resume import ProfessionalExperienceItem
from aimodel.modules.scoring.experience import calculate_experience_score

def test_calculate_experience_score():
    experience = [
        ProfessionalExperienceItem(company="FPT Software", location="Hanoi", position="Software Engineer", seniority="Junior", duration="2 years", description="Developed web applications using Python and Django.")
    ]
    score = calculate_experience_score(experience)
    assert score == 65  # FPT Software (20) + Software Engineer (25) + Description (20)