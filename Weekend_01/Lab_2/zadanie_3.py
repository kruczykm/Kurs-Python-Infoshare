# -----------------------------------------------------------------------------
# ZADANIE 5 – FUNKCJA + IF
# -----------------------------------------------------------------------------
#
# Napisz funkcję:
#
# get_score_category(score)
#
#
# Funkcja powinna zwracać:
#
# "high"
# jeśli score >= 70
#
#
# "medium"
# jeśli score >= 40
#
#
# "low"
# w pozostałych przypadkach.
#
#
# Sprawdź funkcję dla:
#
# 95
# 65
# 30

def get_score_category(score: int) -> str:
    if score >= 70:
        return "high"
    elif score >= 40:
        return "medium"
    else:
        return "low"

print(f"Your category's score is {get_score_category(95)}.")
print(f"Your category's score is {get_score_category(65)}.")
print(f"Your category's score is {get_score_category(30)}.")