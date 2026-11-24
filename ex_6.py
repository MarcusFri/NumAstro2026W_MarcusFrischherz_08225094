import stars as st

sirius = st.Star('Sirius', 2, 3, 8000)
wega = st.Star('Wega', 4, 5, 6000)
rigel = st.Star('Rigel', 4, 5, 7000)
pollux = st.Star('Pollux', 5, 6, 8000)
betelgeuse = st.Star('Betelgeuse', 5, 6, 4000)

stars = [sirius, wega]
star = st.find_star(stars, "Sirius")
print(star)

star = st.find_star(stars, "Beteigeuze")
print(star)

giant_stars = ["Rigel", "Betelgeuse", "Pollux"]

test = [rigel, wega, pollux]
for star in test:
    if star.name in giant_stars and star.temperature > 5000:
        print(f'{star.name} is giant and hot')