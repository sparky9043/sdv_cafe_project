from django.core.management.base import BaseCommand
from menu.models import Category, MenuItem


class Command(BaseCommand):
    help = "Seeds the database with Stardew Valley themed cafe menu items."

    def handle(self, *args, **options):

        # ── Wipe existing data ─────────────────────────────────────────────
        self.stdout.write("  Wiping existing menu data...")
        MenuItem.objects.all().delete()
        Category.objects.all().delete()

        # ── Categories ─────────────────────────────────────────────────────
        drinks = Category.objects.create(name="drink")
        food = Category.objects.create(name="food")
        desserts = Category.objects.create(name="dessert")
        merch = Category.objects.create(name="merch")

        self.stdout.write("  Categories created.")

        # ── Helper ─────────────────────────────────────────────────────────
        def add(category, name, price, description=""):
            MenuItem.objects.create(
                category=category,
                name=name,
                price=price,
                description=description,
            )

        # ── Drinks ────────────────────────────────────────────────────────

        # Hot coffee & espresso
        add(
            drinks,
            "Ancient Fruit Latte",
            6.50,
            "Velvety oat milk latte infused with a syrup made from the rarest fruit in the valley. Sweet, floral, and worth the wait.",
        )
        add(
            drinks,
            "Starfruit Espresso",
            5.50,
            "A double shot of rich espresso brightened with a splash of starfruit citrus concentrate. Tart, bold, and golden.",
        )
        add(
            drinks,
            "Sweet Gem Berry Cappuccino",
            7.00,
            "Frothy cappuccino sweetened with a gem berry reduction. Earthy, berry-forward, and impossibly smooth.",
        )
        add(
            drinks,
            "Pumpkin Spice Latte",
            6.00,
            "Fall harvest pumpkin blended with cinnamon, nutmeg, and steamed milk. A Pelican Town autumn tradition.",
        )
        add(
            drinks,
            "Blueberry Matcha Latte",
            6.50,
            "Ceremonial grade matcha layered over blueberry compote and oat milk. Earthy, sweet, and a little wild.",
        )
        add(
            drinks,
            "Pierre's Morning Blend",
            3.50,
            "The same honest drip coffee Pierre brews before opening the shop. Reliable, warm, no fuss.",
        )
        add(
            drinks,
            "Gus's Special Roast",
            4.50,
            "A dark roast blend served at the Stardrop Saloon since year one. Bold and smoky with a clean finish.",
        )
        add(
            drinks,
            "Sebastian's Pitch Black Espresso",
            4.00,
            "Triple shot, no sugar, no milk. Exactly how Sebastian drinks it in the basement at midnight.",
        )

        # Hot tea
        add(
            drinks,
            "Caroline's Jade Green Tea",
            4.50,
            "Loose leaf green tea brewed from Caroline's secret garden. Delicate, grassy, and quietly restorative.",
        )
        add(
            drinks,
            "Evelyn's Chamomile Tea",
            4.00,
            "Dried chamomile steeped slowly, just like Evelyn taught us. Gentle, golden, and made with love.",
        )
        add(
            drinks,
            "Spice Berry Chai",
            5.50,
            "Foraged spice berries simmered with cardamom, ginger, and black tea. Warming from the first sip.",
        )
        add(
            drinks,
            "Wild Plum Black Tea",
            4.50,
            "Autumn foraged wild plum steeped into a robust black tea. Tart, rich, and deeply seasonal.",
        )
        add(
            drinks,
            "Salmonberry Herbal Tea",
            4.00,
            "A light spring herbal blend built around sweet salmonberries. Floral, mild, and easy to love.",
        )
        add(
            drinks,
            "Cranberry Hibiscus Tea",
            4.50,
            "Tart cranberry and hibiscus flowers steeped together into a ruby-red brew. Bright and refreshing hot or cold.",
        )
        add(
            drinks,
            "Fiddlehead Mint Tea",
            4.00,
            "Fresh mint with a hint of forest fiddlehead. A clean, cool herbal tea with a subtle earthy undertone.",
        )
        add(
            drinks,
            "Keg-Brewed Hops Green Tea",
            4.50,
            "Green tea finished in a keg with a touch of Pelican Town hops. Crisp, slightly bitter, and unexpectedly smooth.",
        )

        # Cold drinks & smoothies
        add(
            drinks,
            "Starfruit Lemonade",
            5.50,
            "Fresh-pressed starfruit juice shaken with house lemonade over ice. Sunshine in a cup.",
        )
        add(
            drinks,
            "Ancient Fruit Smoothie",
            7.00,
            "Blended ancient fruit, banana, and coconut milk. Thick, tropical, and impossibly rare.",
        )
        add(
            drinks,
            "Mango Coconut Cooler",
            6.00,
            "Island mango blended with creamy coconut milk and poured over crushed ice. Sweet, cold, and summery.",
        )
        add(
            drinks,
            "Pineapple Passion Fruit Juice",
            5.50,
            "Cold pressed pineapple and passion fruit. Tangy, tropical, and bright enough to make any day feel like summer.",
        )
        add(
            drinks,
            "Hot Pepper Mango Juice",
            5.00,
            "Fresh mango juice with a slow-building kick of Pelican Town hot pepper. Sweet heat, chilled cold.",
        )
        add(
            drinks,
            "Rhubarb Strawberry Soda",
            5.00,
            "House-made rhubarb and strawberry syrup topped with sparkling water. Tart, sweet, and perfectly pink.",
        )
        add(
            drinks,
            "Red Cabbage Beet Juice",
            5.50,
            "Cold pressed red cabbage and roasted beet. Earthy, vivid, and surprisingly delicious.",
        )
        add(
            drinks,
            "Crystal Fruit Sparkling Water",
            4.50,
            "Still or sparkling water infused with winter crystal fruit. Clean, delicate, and lightly sweet.",
        )
        add(
            drinks,
            "Blueberry Lavender Lemonade",
            5.50,
            "House lemonade infused with blueberry compote and a whisper of lavender. Floral, cool, and beautifully purple.",
        )
        add(
            drinks,
            "Abigail's Purple Butterfly Lemonade",
            6.00,
            "Butterfly pea flower lemonade that shifts from deep blue to violet. Abigail approved. Slightly magical.",
        )
        add(
            drinks,
            "Elliott's Coconut Iced Tea",
            5.50,
            "Black tea sweetened with coconut syrup and served over ice. Refined, smooth, and written by candlelight.",
        )
        add(
            drinks,
            "Sam's Watermelon Slushie",
            5.00,
            "Blended fresh watermelon poured over shaved ice. Cold, sweet, and exactly what you want after a hot day in the mines.",
        )
        add(
            drinks,
            "Robin's Cranberry Spritz",
            5.50,
            "Cranberry juice, a squeeze of lime, and sparkling water. Simple, clean, and built to last.",
        )
        add(
            drinks,
            "Haley's Iced Honey Oat Latte",
            6.00,
            "Cold espresso over oat milk sweetened with local wildflower honey. Smooth, golden, and surprisingly chic.",
        )
        add(
            drinks,
            "Melon Agua Fresca",
            5.00,
            "Fresh melon blended with water, lime, and a pinch of salt. Light, hydrating, and deeply refreshing.",
        )
        add(
            drinks,
            "Pale Ale (Brewed on Premise)",
            7.00,
            "A small-batch pale ale brewed in-house with Pelican Town hops. Crisp, hoppy, and pairs well with anything on the menu.",
        )
        add(
            drinks,
            "Void Spirit Cold Brew",
            5.50,
            "Steeped for 20 hours in cold water. Deeply dark, zero bitterness, and a caffeine level we won't specify.",
        )
        add(
            drinks,
            "Sandy's Desert Rose Lemonade",
            5.50,
            "Rose water and lemonade inspired by Sandy's shop in the Calico Desert. Fragrant, light, and a long way from home.",
        )

        self.stdout.write(
            f"  Drinks created: {MenuItem.objects.filter(category=drinks).count()}"
        )

        # ── Food ──────────────────────────────────────────────────────────
        add(
            food,
            "Marnie's Farmhouse Egg Omelette",
            12.00,
            "A fluffy three-egg omelette made with Marnie's ranch eggs, sharp cheddar, and fresh chives. Simple and honest.",
        )
        add(
            food,
            "Harvey's Parsnip & Arugula Salad",
            10.00,
            "Roasted parsnips over a bed of peppery arugula with lemon vinaigrette. Doctor-approved. Genuinely good.",
        )
        add(
            food,
            "Leah's Fiddlehead Fern Toast",
            13.00,
            "Sautéed fiddlehead ferns on thick sourdough with herb cream cheese. Foraged this morning, made with care.",
        )
        add(
            food,
            "Penny's Kale Caesar Wrap",
            11.00,
            "Kale tossed in house Caesar dressing with croutons and parmesan, wrapped tight. Quiet, filling, and good.",
        )
        add(
            food,
            "Willy's Smoked Salmon Bagel",
            14.00,
            "House-smoked salmon with cream cheese, capers, and red onion on a toasted everything bagel.",
        )
        add(
            food,
            "Maru's Grilled Veggie Panini",
            12.00,
            "Zucchini, roasted peppers, and mozzarella pressed on ciabatta. Engineered for maximum flavour efficiency.",
        )
        add(
            food,
            "Gus's Hot Pepper Popper Sandwich",
            13.00,
            "Crispy hot pepper poppers stacked on a brioche roll with chipotle aioli. The Saloon's best kept secret.",
        )
        add(
            food,
            "Ancient Fruit & Brie Flatbread",
            15.00,
            "Thin crust flatbread topped with ancient fruit jam, creamy brie, and fresh thyme. Rare and worth every coin.",
        )
        add(
            food,
            "Starfruit Chicken Salad Wrap",
            13.00,
            "Grilled chicken, starfruit chunks, and greens in a honey-lime dressing. Bright, filling, and a little bit fancy.",
        )
        add(
            food,
            "Pumpkin Soup & Sourdough",
            12.00,
            "Roasted pumpkin blended into a velvety soup served with a thick slice of house sourdough. Autumn in a bowl.",
        )
        add(
            food,
            "Bok Choy & Tofu Rice Bowl",
            11.00,
            "Steamed bok choy and crispy tofu over jasmine rice with a sesame-ginger glaze. Light, clean, and satisfying.",
        )
        add(
            food,
            "Cauliflower & Potato Frittata",
            12.00,
            "Oven-baked frittata with roasted cauliflower, potato, and gruyère. Served warm in wedges.",
        )
        add(
            food,
            "Red Cabbage Apple Slaw Sandwich",
            11.00,
            "House-made red cabbage and apple slaw piled onto a soft roll with whole grain mustard. Crunchy and bright.",
        )
        add(
            food,
            "Artichoke Spinach Melt",
            13.00,
            "Warm artichoke and spinach dip melted into an open-faced sourdough melt. Creamy, golden, irresistible.",
        )
        add(
            food,
            "Mayor Lewis's Truffle Avocado Toast",
            14.00,
            "Thick sourdough with smashed avocado and a drizzle of black truffle oil. He didn't share the recipe but we figured it out.",
        )
        add(
            food,
            "Linus's Wild Mushroom Toast",
            12.00,
            "Forest mushrooms sautéed in garlic butter on toasted rye. Foraged respectfully. Linus would approve.",
        )
        add(
            food,
            "Eggplant Parmesan Melt",
            13.00,
            "Breaded eggplant layered with marinara and melted mozzarella on a hoagie roll. Crispy, saucy, and satisfying.",
        )
        add(
            food,
            "Krobus's Void Mushroom Risotto",
            16.00,
            "Creamy risotto made with rare void mushrooms from the sewers. Deeply savoury. Don't ask where he got them.",
        )
        add(
            food,
            "Wizard's Yam & Kale Hash",
            12.00,
            "Roasted yam and crispy kale hash with a soft-poached egg. Prepared during the new moon for best results.",
        )
        add(
            food,
            "Pam's Corn & Cheese Quesadilla",
            11.00,
            "Grilled corn and melted cheese folded into a crispy quesadilla. Simple, golden, ready when the bus is.",
        )

        self.stdout.write(
            f"  Food created: {MenuItem.objects.filter(category=food).count()}"
        )

        # ── Desserts ──────────────────────────────────────────────────────
        add(
            desserts,
            "Ancient Fruit Tart",
            8.00,
            "Buttery tart shell filled with custard and topped with sliced ancient fruit. As rare as it is delicious.",
        )
        add(
            desserts,
            "Starfruit Cheesecake Slice",
            9.00,
            "New York style cheesecake with a starfruit curd topping. Tangy, rich, and golden.",
        )
        add(
            desserts,
            "Sweet Gem Berry Macaron",
            7.50,
            "French macaron shells sandwiched with sweet gem berry buttercream. Small, precious, and perfect.",
        )
        add(
            desserts,
            "Melon Panna Cotta",
            8.50,
            "Silky panna cotta set in a melon purée base with a drizzle of honey. Elegant and lightly sweet.",
        )
        add(
            desserts,
            "Blueberry Lavender Scone",
            6.50,
            "Flaky butter scone studded with blueberries and scented with lavender. Best with a cup of green tea.",
        )
        add(
            desserts,
            "Evelyn's Grandma Cookie",
            5.50,
            "A soft, golden chocolate chip cookie baked from Evelyn's original recipe. Tastes like being welcomed home.",
        )
        add(
            desserts,
            "Strawberry Rhubarb Pie Slice",
            7.50,
            "Classic double-crust pie with sweet strawberries and tart rhubarb. Served warm. The valley's favourite.",
        )
        add(
            desserts,
            "Pumpkin Roll Cake",
            7.00,
            "Spiced pumpkin sponge rolled around a cream cheese filling. A fall harvest staple, available all year.",
        )
        add(
            desserts,
            "Cranberry Orange Muffin",
            5.00,
            "A tall, domed muffin with tart cranberries and bright orange zest. Perfect with your morning coffee.",
        )
        add(
            desserts,
            "Wild Plum & Almond Tart",
            8.00,
            "Fall foraged wild plums over a frangipane almond cream in a shortcrust shell. Rustic and beautifully rich.",
        )

        self.stdout.write(
            f"  Desserts created: {MenuItem.objects.filter(category=desserts).count()}"
        )

        # ── Merch ─────────────────────────────────────────────────────────
        add(
            merch,
            "Pelican Town Ceramic Mug",
            18.00,
            "A hand-glazed ceramic mug with the Pelican Town crest. Dishwasher safe. Holds 12oz of whatever gets you through the day.",
        )
        add(
            merch,
            "Stardrop Saloon Pint Glass",
            16.00,
            "Official Stardrop Saloon branded pint glass. Gus uses these. Now you can too.",
        )
        add(
            merch,
            "Year One Farmer Tumbler",
            20.00,
            "Insulated stainless steel tumbler with a 'Year One Farmer' emboss. Keeps drinks cold for 24 hours, hot for 12.",
        )
        add(
            merch,
            "Ancient Fruit Enamel Pin",
            8.00,
            "A small, detailed enamel pin of the ancient fruit. Gold backing, butterfly clutch. Limited run.",
        )
        add(
            merch,
            "Junimo Plush Keychain",
            12.00,
            "A soft miniature Junimo in your choice of colour. Clip it to your bag. They like coming along.",
        )
        add(
            merch,
            "Stardew Farm Co. Tote Bag",
            20.00,
            "A sturdy canvas tote printed with the Stardew Farm Co. logo. Holds a week's worth of groceries or a very full harvest.",
        )
        add(
            merch,
            "Seasonal Harvest Postcard Set",
            10.00,
            "A set of four illustrated postcards — one per season. Painted by a local Pelican Town artist.",
        )
        add(
            merch,
            "Pelican Town Map Print",
            18.00,
            "A detailed illustrated map of Pelican Town and surrounds. Printed on heavyweight paper. Frame it or fold it.",
        )
        add(
            merch,
            "Robin's Carpentry Wooden Spoon Set",
            15.00,
            "A set of two hand-turned wooden spoons made in Robin's style. Sanded smooth, ready for your kitchen.",
        )
        add(
            merch,
            "My First Harvest Seed Packet",
            6.00,
            "A curated seed packet with spring crops to get you started. Includes a small card with planting notes.",
        )

        self.stdout.write(
            f"  Merch created: {MenuItem.objects.filter(category=merch).count()}"
        )

        total = MenuItem.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Done! {total} menu items across {Category.objects.count()} categories."
            )
        )
