import numpy as np
from statistics import mean
import unittest

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

class Department:
    def __init__(self, name, mean_threat, variance, num_users, importance):
        self.name = name
        self.threat_scores = generate_random_data(mean_threat, variance, num_users)
        self.importance = importance

    def avg_threat_score(self):
        if len(self.threat_scores) > 0:
            return mean(self.threat_scores)
        else:
            return 0

class CompanySecurityScore:
    def __init__(self, departments):
        self.departments = departments

    def calculate_aggregated_score(self):
        weighted_sum = 0
        total_weight = 0

        for dept in self.departments:
            avg_score = dept.avg_threat_score()
            weight = dept.importance
            weighted_sum += avg_score * weight
            total_weight += weight

        if total_weight:
            return min(max(weighted_sum / total_weight, 0), 90)
        else:
            return 0

class TestDepartment(unittest.TestCase):
    def test_avg_threat_score_non_empty(self):
        dept = Department("TestDept", 30, 10, 5, 3)
        self.assertGreaterEqual(dept.avg_threat_score(), 0)
        self.assertLessEqual(dept.avg_threat_score(), 90)

    def test_avg_threat_score_empty(self):
        dept = Department("EmptyDept", 30, 10, 0, 3)
        self.assertEqual(dept.avg_threat_score(), 0)

class TestCompanySecurityScore(unittest.TestCase):
    def test_calculate_aggregated_score_equal_importance(self):
        departments = [
            Department("Engineering", 30, 5, 10, 3),
            Department("Marketing", 30, 5, 10, 3),
            Department("Finance", 30, 5, 10, 3),
            Department("HR", 30, 5, 10, 3),
            Department("Science", 30, 5, 10, 3)
        ]
        company_score = CompanySecurityScore(departments)
        score = company_score.calculate_aggregated_score()
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_calculate_aggregated_score_varying_importance(self):
        departments = [
            Department("Engineering", 50, 10, 10, 5),
            Department("Marketing", 20, 5, 10, 1),
            Department("Finance", 40, 20, 10, 4),
            Department("HR", 10, 3, 10, 2),
            Department("Science", 30, 5, 10, 3)
        ]
        company_score = CompanySecurityScore(departments)
        score = company_score.calculate_aggregated_score()
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_calculate_aggregated_score_high_threat(self):
        departments = [
            Department("Engineering", 80, 5, 10, 5),
            Department("Marketing", 80, 5, 10, 4),
            Department("Finance", 80, 5, 10, 3),
            Department("HR", 80, 5, 10, 2),
            Department("Science", 80, 5, 10, 1)
        ]
        company_score = CompanySecurityScore(departments)
        score = company_score.calculate_aggregated_score()
        self.assertGreaterEqual(score, 75)

    def test_calculate_aggregated_score_low_threat(self):
        departments = [
            Department("Engineering", 5, 2, 10, 5),
            Department("Marketing", 5, 2, 10, 4),
            Department("Finance", 5, 2, 10, 3),
            Department("HR", 5, 2, 10, 2),
            Department("Science", 5, 2, 10, 1)
        ]
        company_score = CompanySecurityScore(departments)
        score = company_score.calculate_aggregated_score()
        self.assertLessEqual(score, 15)

if __name__ == "__main__":
    unittest.main()

