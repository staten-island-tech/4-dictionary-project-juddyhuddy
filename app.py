# You will be creating a little store in your terminal. You will have a list of
# dictionaries that will be displayed to the user. Each Dictionary will have at
# least 3 properties (name, price and whatever you want)
# PART ONE:
# The user will select one item to purchase. You will then show the user
# ONLY the name of the item they purchased. You will need to use the item
# index to accomplish this task.

# PART TWO:
# You will now make the app more complex by incorporating while loops and
# a “cart”. Users will be shown the list of items and asked to purchase one.
# Afterwards ask the user if they wish to continue. Once the user has decided
# they are done shopping, print the names of the items purchased and the
# total of the cart.

maison_margiela_item = [{
    "name": "Replica Under the Stars eau de toilette",
    "price": 170,
    "department": "Fragrances",
    "description": "Replica Under the Stars eau de toilette evokes the memory of a starry night spent in the wilds of nature. A timeless blend of oud essence and labdanum resinoid notes recalls a dark, mystical night; with raw and leather accord bringing an element of the untamed. Black pepper essence then serves as a reminder of the captivating experience of immersing oneself in nature. Size 100ml."
},
{
    "name": "MM X Gentle Monster MM220 A030(N)",
    "price": 470,
    "department": "Sunglasses",
    "description": "The third Maison Margiela x Gentle Monster collaboration is rooted at the intersection of classicism and futurism. The MM220 A030(N) sunglasses feature an oval front and a cable temple; originally designed to prevent slipping, now reimagined beyond functionality to express a fresh yet sophisticated aesthetic. The design is complete with industrial hardware details and the Maison Margiela logo engraved onto metal plates."

},
{   "name": "Denim Shirt",
    "price": 1295,
    "department": "Shirt",
    "description": "This shirt in Japanese denim embraces workwear origins and reinterprets them through a lived-in finish. Fading, tonal repair marks and softened seams infuse a sense of continuity, while straight lines and a Memory of pocket define the design. At the back, the Maisons signature four stitches appear; the opposite of a label."
},
{ "name": "5AC loved to death medium",
    "price": 3160,
    "department": "",
    "description": "This shirt in Japanese denim embraces workwear origins and reinterprets them through a lived-in finish. Fading, tonal repair marks and softened seams infuse a sense of continuity, while straight lines and a Memory of pocket define the design. At the back, the Maisons signature four stitches appear; the opposite of a label."
},
{
    "name": "5AC Classique Baby Bag",
    "price": 1890,
    "department": "Bag",
    "description": "The 5AC Classique Baby bag is crafted in grained calf leather with a structured silhouette and top handles. The design explores the Maisons Anonymity of the Lining concept with an exposed lining and zip closure. Finished with the numeric logo label and the iconic four white stitches at the back."
},
{
    "name": "Glam Slam Red Carpet Bag",
    "price": 2450,
    "department": "Bag",
    "description": "The Glam Slam Red Carpet bag is defined by its quilted nappa leather construction inspired by matelassé techniques. Soft and pillowy in texture, it features a chain strap and the Maisons numeric logo detail, embodying comfort and couture craftsmanship."
},
{
    "name": "Snatched Small Top-Handle Bag",
    "price": 2190,
    "department": "Bag",
    "description": "The Snatched Small bag is designed with sharp architectural lines and a distinctive cut-out handle. Crafted in smooth leather, it can be worn by hand or crossbody and is accented with the Maisons signature four stitches at the back."
},
{
    "name": "Tabi Leather Ankle Boots",
    "price": 1290,
    "department": "Shoes",
    "description": "The iconic Tabi ankle boots are crafted in soft leather with a cylindrical heel and the Maisons signature split-toe silhouette inspired by traditional Japanese socks. Hand-finished details highlight the artisanal heritage of the design."
},
{
    "name": "Replica Leather Sneakers",
    "price": 620,
    "department": "Shoes",
    "description": "Replica sneakers reinterpret classic Austrian sports footwear from the 1970s. Made in smooth calf leather with suede panels, they feature a gum sole and subtle branding, finished with the Maisons signature stitch detail."
},
{
    "name": "Evolution Low-Top Sneakers",
    "price": 690,
    "department": "Shoes",
    "description": "The Evolution low-top sneakers combine technical mesh, leather and suede for a dynamic layered look. Set on a lightweight sole, they reflect the Maisons contemporary approach to athletic design."
},
{
    "name": "Four Stitches Card Holder",
    "price": 295,
    "department": "Small Leather Goods",
    "description": "Crafted in grained leather, the Four Stitches card holder features multiple card slots and the Maisons iconic four white stitches at the back  the opposite of a label  emphasizing anonymity and understated luxury."
},
{
    "name": "Numeric Logo Bifold Wallet",
    "price": 495,
    "department": "Small Leather Goods",
    "description": "This bifold wallet is made in supple calf leather and detailed with the Maisons numeric logo inside. Designed with multiple compartments for cards and cash, it combines functionality with minimalist aesthetics."
},
{
    "name": "Décortiqué Wool Blazer",
    "price": 1895,
    "department": "Clothing",
    "description": "The Décortiqué wool blazer reinterprets classic tailoring through exposed seams and layered construction. Crafted in fine wool, it reflects the Maisons deconstruction ethos while maintaining a refined silhouette."
},
{
    "name": "Oversized Knit Sweater",
    "price": 990,
    "department": "Clothing",
    "description": "This oversized knit sweater is spun from a soft wool blend and designed with dropped shoulders and ribbed trims. The relaxed silhouette is subtly marked with the Maison’s four stitches at the back."
},
{
    "name": "Paint Splatter Denim Jeans",
    "price": 850,
    "department": "Clothing",
    "description": "Crafted in classic five-pocket denim, these jeans feature hand-applied paint splatter detailing, making each piece unique. The design reflects the Maison’s artisanal approach and experimental spirit."
},
{
    "name": "Replica By the Fireplace Eau de Toilette 100ml",
    "price": 160,
    "department": "Fragrance",
    "description": "Replica By the Fireplace captures the memory of a cozy winter evening with notes of chestnut accord, clove oil and vanilla. The warm and smoky composition evokes comfort and familiarity."
},
{
    "name": "Replica Jazz Club Eau de Toilette 100ml",
    "price": 160,
    "department": "Fragrance",
    "description": "Replica Jazz Club recalls the ambiance of a Brooklyn jazz bar with notes of rum, tobacco leaf and vanilla bean. Rich and intoxicating, it balances warmth with refined sweetness."
},
{
    "name": "Glam Slam Sport Backpack",
    "price": 1990,
    "department": "Bag",
    "description": "The Glam Slam Sport backpack is crafted in quilted nylon with a padded silhouette inspired by travel and leisure. Designed with adjustable straps and a front logo patch, it combines practicality with signature Maison codes."
},
{
    "name": "Tabi Ballerina Flats",
    "price": 890,
    "department": "Shoes",
    "description": "The Tabi ballerina flats reinterpret the Maison’s iconic split-toe design in a delicate ballet silhouette. Made in supple leather with a slim sole, they embody avant-garde tradition and timeless elegance."
}
]

# You will now make the app more complex by incorporating while loops and
# a “cart”. Users will be shown the list of items and asked to purchase one.
# Afterwards ask the user if they wish to continue. Once the user has decided
# they are done shopping, print the names of the items purchased and the
# total of the cart.

for index, item in enumerate(maison_margiela_item):
    print(index, ":", item)
choice = int(input("Item Number?"))
print(maison_margiela_item[choice]['name'])
x = (input("continue?"))
while x == ("yes"):
    choice = int(input("Item Number?"))
    print(maison_margiela_item[choice]['name'])
    x = (input("continue?"))
if x == ("no"):
    print("okay")


    
    
    
    