# Alice	USA
# Francois	Canada
# Inti	Peru
# Monika	Germany
# Sanyu	Uganda
# Yoshitaka	Japan

person_residency = dict(Alice='USA', Francois='Canada', Inti='Peru', Monika='Germany', Sanyu='Uganda', Yoshitaka='Japan')
names = list(person_residency)
for k, v in person_residency.items():
    print(f"{k} lives in {v}")

