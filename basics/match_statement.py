# Let's define a function that uses match/case
def match_response(http_status_code):
    match http_status_code:
        case 200 | 201 | 202 | 204 as status:
            return f"HTTP good, returned {status}"
        case 400 | 401 | 403 | 404 as status:
            return f"Something wrong: {status}"
        case 500 as status:
            return f"Server error with code: {status}"
        case _ as status:
            return f"Unknown status code: {status}"

# If 200
print(match_response(200))

# If 404
print(match_response(404))

# If 500
print(match_response(500))

# 600 is not a valid status code
print(match_response(600))

cities = [
    ('London', (51.5085300, -0.1257400)),
    ('Rome', (41.8919300, 12.5113300)),
    ('Paris', (48.8534100, 2.3488000))
]

# Match/case
for city in cities:
    match city:
        case [name, (lat, lon)]:
            print(f'City: {name}, lat:{lat:.2f}, lon:{lon:.2f}')

# We can also add an optional guard with an if
# Prints only cities with lon > 0
for city in cities:
    match city:
        case [name, (lat, lon)] if lon > 0:
            print(f'City: {name}, lat:{lat:.2f}, lon:{lon:.2f}')