from django.core.management.base import BaseCommand
from menu.models import Category, MenuItem


class Command(BaseCommand):
    help = "Seeds the database with Stardew Valley themed cafe menu items."

    def handle(self, *args, **options):

        # ── Categories ─────────────────────────────────────────────────────
        drinks = Category.objects.create(name="drink")
        food = Category.objects.create(name="food")
        desserts = Category.objects.create(name="dessert")
        merch = Category.objects.create(name="merch")

        self.stdout.write("  Categories created.")

        # ── Helper ─────────────────────────────────────────────────────────
        def add(category, name, price):
            MenuItem.objects.create(category=category, name=name, price=price)

        # ── Drinks (34 items) ──────────────────────────────────────────────

        # Hot coffee & espresso
        add(drinks, "Ancient Fruit Latte", 6.50)
        add(drinks, "Starfruit Espresso", 5.50)
        add(drinks, "Sweet Gem Berry Cappuccino", 7.00)
        add(drinks, "Pumpkin Spice Latte", 6.00)
        add(drinks, "Blueberry Matcha Latte", 6.50)
        add(drinks, "Pierre's Morning Blend", 3.50)
        add(drinks, "Gus's Special Roast", 4.50)
        add(drinks, "Sebastian's Pitch Black Espresso", 4.00)

        # Hot tea
        add(drinks, "Caroline's Jade Green Tea", 4.50)
        add(drinks, "Evelyn's Chamomile Tea", 4.00)
        add(drinks, "Spice Berry Chai", 5.50)
        add(drinks, "Wild Plum Black Tea", 4.50)
        add(drinks, "Salmonberry Herbal Tea", 4.00)
        add(drinks, "Cranberry Hibiscus Tea", 4.50)
        add(drinks, "Fiddlehead Mint Tea", 4.00)
        add(drinks, "Keg-Brewed Hops Green Tea", 4.50)

        # Cold drinks & smoothies
        add(drinks, "Starfruit Lemonade", 5.50)
        add(drinks, "Ancient Fruit Smoothie", 7.00)
        add(drinks, "Mango Coconut Cooler", 6.00)
        add(drinks, "Pineapple Passion Fruit Juice", 5.50)
        add(drinks, "Hot Pepper Mango Juice", 5.00)
        add(drinks, "Strawberry Rhubarb Soda", 5.00)
        add(drinks, "Red Cabbage Beet Juice", 5.50)
        add(drinks, "Crystal Fruit Sparkling Water", 4.50)
        add(drinks, "Blueberry Lavender Lemonade", 5.50)
        add(drinks, "Abigail's Purple Butterfly Lemonade", 6.00)
        add(drinks, "Elliott's Coconut Iced Tea", 5.50)
        add(drinks, "Sam's Watermelon Slushie", 5.00)
        add(drinks, "Robin's Cranberry Spritz", 5.50)
        add(drinks, "Haley's Iced Coconut Honey Latte", 6.00)
        add(drinks, "Melon Agua Fresca", 5.00)
        add(drinks, "Pale Ale (Brewed on Premise)", 7.00)
        add(drinks, "Void Spirit Cold Brew", 5.50)
        add(drinks, "Sandy's Desert Rose Lemonade", 5.50)

        self.stdout.write(
            f"  Drinks created: {MenuItem.objects.filter(category=drinks).count()}"
        )

        # ── Food (20 items) ────────────────────────────────────────────────
        add(food, "Marnie's Farmhouse Egg Omelette", 12.00)
        add(food, "Harvey's Parsnip & Arugula Salad", 10.00)
        add(food, "Leah's Fiddlehead Fern Toast", 13.00)
        add(food, "Penny's Kale Caesar Wrap", 11.00)
        add(food, "Willy's Smoked Salmon Bagel", 14.00)
        add(food, "Maru's Grilled Veggie Panini", 12.00)
        add(food, "Gus's Hot Pepper Popper Sandwich", 13.00)
        add(food, "Ancient Fruit & Brie Flatbread", 15.00)
        add(food, "Starfruit Chicken Salad Wrap", 13.00)
        add(food, "Pumpkin Soup & Sourdough", 12.00)
        add(food, "Bok Choy & Tofu Rice Bowl", 11.00)
        add(food, "Cauliflower & Potato Frittata", 12.00)
        add(food, "Red Cabbage Apple Slaw Sandwich", 11.00)
        add(food, "Artichoke Spinach Melt", 13.00)
        add(food, "Mayor Lewis's Truffle Avocado Toast", 14.00)
        add(food, "Linus's Wild Mushroom Toast", 12.00)
        add(food, "Eggplant Parmesan Melt", 13.00)
        add(food, "Krobus's Void Mushroom Risotto", 16.00)
        add(food, "Wizard's Yam & Kale Hash", 12.00)
        add(food, "Pam's Corn & Cheese Quesadilla", 11.00)

        self.stdout.write(
            f"  Food created: {MenuItem.objects.filter(category=food).count()}"
        )

        # ── Desserts (10 items) ────────────────────────────────────────────
        add(desserts, "Ancient Fruit Tart", 8.00)
        add(desserts, "Starfruit Cheesecake Slice", 9.00)
        add(desserts, "Sweet Gem Berry Macaron", 7.50)
        add(desserts, "Melon Panna Cotta", 8.50)
        add(desserts, "Blueberry Lavender Scone", 6.50)
        add(desserts, "Evelyn's Grandma Cookie", 5.50)
        add(desserts, "Strawberry Rhubarb Pie Slice", 7.50)
        add(desserts, "Pumpkin Roll Cake", 7.00)
        add(desserts, "Cranberry Orange Muffin", 5.00)
        add(desserts, "Wild Plum & Almond Tart", 8.00)

        self.stdout.write(
            f"  Desserts created: {MenuItem.objects.filter(category=desserts).count()}"
        )

        # ── Merch (10 items) ───────────────────────────────────────────────
        add(merch, "Pelican Town Ceramic Mug", 18.00)
        add(merch, "Stardrop Saloon Pint Glass", 16.00)
        add(merch, "Year One Farmer Tumbler", 20.00)
        add(merch, "Ancient Fruit Enamel Pin", 8.00)
        add(merch, "Junimo Plush Keychain", 12.00)
        add(merch, "Stardew Farm Co. Tote Bag", 20.00)
        add(merch, "Seasonal Harvest Postcard Set", 10.00)
        add(merch, "Pelican Town Map Print", 18.00)
        add(merch, "Robin's Carpentry Wooden Spoon Set", 15.00)
        add(merch, "My First Harvest Seed Packet", 6.00)

        self.stdout.write(
            f"  Merch created: {MenuItem.objects.filter(category=merch).count()}"
        )

        total = MenuItem.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Done! {total} menu items across {Category.objects.count()} categories."
            )
        )
