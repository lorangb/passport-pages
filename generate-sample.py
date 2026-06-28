from fpdf import FPDF
import os

class BookPDF(FPDF):
    def __init__(self):
        super().__init__()
        # Register Unicode font for special characters
        self.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
        self.add_font('DejaVu', 'B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', uni=True)
        self.add_font('DejaVu', 'I', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', uni=True)
    
    def header(self):
        if self.page_no() > 1:
            self.set_font("DejaVu", 'I', 7)
            self.set_text_color(140, 140, 140)
            self.cell(0, 8, 'Passport Pages - Sample Book', align='L')
            self.cell(0, 8, f'Page {self.page_no()}', align='R', new_x='LMARGIN', new_y='NEXT')
            self.line(10, 14, 200, 14)
            self.ln(4)
    
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("DejaVu", 'I', 6)
            self.set_text_color(180, 180, 180)
            self.cell(0, 10, 'Passport Pages - The world is their story. | passportpages.com', align='C')
    
    def chapter_title(self, title):
        self.set_font("DejaVu", 'B', 18)
        self.set_text_color(27, 42, 74)
        self.cell(0, 12, title, new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(212, 115, 94)
        self.line(10, self.get_y(), 80, self.get_y())
        self.ln(6)
    
    def sub_title(self, title):
        self.set_font("DejaVu", 'B', 13)
        self.set_text_color(212, 115, 94)
        self.cell(0, 8, title, new_x='LMARGIN', new_y='NEXT')
        self.ln(2)
    
    def fact_box(self, icon, title, text):
        self.set_fill_color(250, 248, 245)
        self.set_draw_color(212, 115, 94)
        x = self.get_x()
        y = self.get_y()
        
        self.set_font("DejaVu", '', 9)
        lines = self.multi_cell(160, 4.5, text, split_only=True)
        box_h = max(20, len(lines) * 4.5 + 12)
        
        if y + box_h > 270:
            self.add_page()
            y = self.get_y()
        
        self.rect(x, y, 170, box_h, style='DF')
        
        self.set_xy(x + 4, y + 4)
        self.set_font("DejaVu", '', 16)
        self.cell(10, 8, icon)
        
        self.set_xy(x + 18, y + 3)
        self.set_font("DejaVu", 'B', 9)
        self.set_text_color(27, 42, 74)
        self.cell(140, 5, title)
        
        self.set_xy(x + 18, y + 9)
        self.set_font("DejaVu", '', 8)
        self.set_text_color(90, 103, 120)
        self.multi_cell(140, 4.5, text)
        
        self.set_y(y + box_h + 4)

pdf = BookPDF()
pdf.set_auto_page_break(auto=True, margin=20)

# Cover
pdf.add_page()
pdf.ln(60)
pdf.set_font("DejaVu", 'B', 32)
pdf.set_text_color(212, 115, 94)
pdf.cell(0, 15, 'Brighton and the Cotswolds', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.set_font("DejaVu", '', 16)
pdf.set_text_color(27, 42, 74)
pdf.cell(0, 10, '~ A Family Adventure ~', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(8)
pdf.set_draw_color(212, 168, 75)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.ln(10)
pdf.set_font("DejaVu", 'I', 11)
pdf.set_text_color(90, 103, 120)
pdf.cell(0, 7, 'Middle Explorer Edition - Ages 9-12', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 7, 'Summer 2026', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(40)
pdf.set_font("DejaVu", '', 8)
pdf.set_text_color(180, 180, 180)
pdf.cell(0, 6, 'PASSPORT PAGES - The world is their story.', align='C', new_x='LMARGIN', new_y='NEXT')

# Welcome
pdf.add_page()
pdf.chapter_title('Welcome, Adventurers!')
pdf.set_font("DejaVu", '', 10)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5.5, "Welcome to Britain! You are about to explore a country packed with more history, weirdness, and wonder per square mile than almost anywhere on Earth. This book is your guide to all the secret stories hiding in the places you will visit.\n\nBefore we start, a few things to keep in mind:")
pdf.ln(4)
facts = [
    'England is smaller than Louisiana but has over 1,000 years of castle history.',
    'The British drive on the LEFT. Look right, then left before crossing!',
    'The UK is made of four countries: England, Scotland, Wales, and Northern Ireland.',
    'Over 30 million people visit the UK each year. Soon, that includes YOU!',
]
for f in facts:
    pdf.set_font("DejaVu", '', 9)
    pdf.set_text_color(90, 103, 120)
    pdf.cell(5, 5, chr(0x2022))
    pdf.multi_cell(165, 5, f)
    pdf.ln(1)

# Brighton
pdf.add_page()
pdf.chapter_title('Brighton - London-by-the-Sea')
pdf.sub_title('The Pebble Beach Surprise')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "Here is something that surprises almost everyone: Brighton Beach does not have sand. It is covered in millions of smooth, round PEBBLES. When the tide comes in, the waves make a strange, rattling sound as they pull the stones back. It is called the shingle music and people come from all over just to hear it.")

pdf.fact_box('S', 'Why Are There No Sandy Beaches?',
    'Brighton sits on a layer of chalk from the South Downs. The waves smash the chalk into tiny bits, but instead of turning into sand, it gets washed away, leaving behind the flint stones. These pebbles have been rolling around in the English Channel for thousands of years. Some of them might have been walked on by Roman soldiers!')

pdf.fact_box('P', 'The Palace Pier - A Victorian Theme Park',
    'Brighton Palace Pier opened in 1899. It is 1,760 feet long - exactly one-third of a mile. During WWII, the pier was closed and the middle section was REMOVED to stop enemy boats from landing on it.')

pdf.sub_title('The Royal Pavilion - A Palace from a Fairy Tale')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "King George IV built this bizarre, beautiful palace in the early 1800s. It looks like an Indian temple but is decorated inside like a Chinese emperor's palace. The dining room table could seat 80 people and was designed so servants could raise and lower the table through a trapdoor to swap courses without being seen!")

# Oxford
pdf.add_page()
pdf.chapter_title('Oxford - The City of Dreaming Spires')
pdf.sub_title('Lunch at The Bear Inn (Est. 1242)')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "The Bear Inn claims to be Oxford's oldest pub, built in 1242. That is over 780 years ago! It opened just 27 years after the Magna Carta was signed. University students have been eating here since before Shakespeare was born.")

pdf.fact_box('B', 'Punting on the River Cherwell',
    'Punting is one of Oxford most beloved traditions. You stand on a flat-bottomed boat and push it along with a long pole. It looks easy but most first-timers end up soaking wet! The tradition dates back to the 1800s. Punts are hired from Magdalen Bridge Boathouse. Magdalen is pronounced MAUD-len.')

pdf.fact_box('L', 'The Bodleian Library',
    "Founded in 1602, the Bodleian has over 13 MILLION books stored across 80 miles of shelves. For centuries, any book published in the UK must be given to the Bodleian for free. That is the law. Every book you have ever read in Britain is probably sitting somewhere in those underground tunnels.")

# Cotswolds
pdf.add_page()
pdf.chapter_title('The Cotswolds - Golden Treasure')
pdf.sub_title('Moreton-in-Marsh and The Tuesday Market')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "Every Tuesday, the High Street transforms into the biggest street market in the Cotswolds. Over 200 stalls sell local produce, antiques, and artisan goods. This tradition dates back to 1226, when King Henry III granted the town a charter. For 800 YEARS, people have been gathering here every Tuesday!")

pdf.add_page()
pdf.chapter_title('Bibury - The Most Beautiful Village')
pdf.sub_title('Arlington Row - The Passport Cottages')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "These honey-colored stone cottages were built in 1380 as a wool store. Monks stored their wool here before selling it across Europe. In the 1600s, they were turned into weavers' cottages. Today, they appear on the INSIDE COVER of every single UK passport.")

pdf.add_page()
pdf.chapter_title("Diddly Squat and Stow-on-the-Wold")
pdf.sub_title("St Edward's Church - The Doors of Durin?")
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "The north door of St Edward's Church is framed by two ancient yew trees whose gnarled roots arch over the entrance like a doorway from a fantasy novel. Many visitors say it looks like the Doors of Durin from Lord of the Rings. The church dates to before 1086. It is mentioned in the Domesday Book!")

pdf.fact_box('F', 'The Domesday Book (1086)',
    "William the Conqueror ordered a massive survey of every piece of land, animal, and person in England. The entry for Stow says: 'King William holds it. 10 hides. 30 villagers. A church. 3 fisheries worth 1000 eels.'")

pdf.sub_title("Diddly Squat Farm Shop")
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "Jeremy Clarkson bought a farm in the Cotswolds in 2008 and discovered he had NO IDEA how to run it. The TV show Clarkson's Farm follows his hilarious failures. The name Diddly Squat means, well, nothing at all - which is what Clarkson knew about farming when he started!")

# Bourton-on-the-Water
pdf.add_page()
pdf.chapter_title('Bourton-on-the-Water')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "Known as the Venice of the Cotswolds for its low stone bridges spanning the shallow River Windrush. Five stone bridges have been here for over 200 years.")

pdf.fact_box('M', 'The Model Village',
    'Bourton has a Model Village - a 1/9th scale replica of the village itself, built in 1937. But here is the mind-bender: the Model Village contains a model of the Model Village. And that model contains a model of THAT model!')

# Stratford-upon-Avon
pdf.add_page()
pdf.chapter_title('Stratford-upon-Avon - Shakespeare')
pdf.sub_title('The Boy from Stratford')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "William Shakespeare was born here in 1564. He went to the local grammar school where he studied Latin, Greek, and rhetoric. His classroom STILL EXISTS. He invented over 1,700 words we still use, including: eyeball, gossip, bedroom, lonely, and swagger.")

pdf.fact_box('T', 'Shakespeare by the Numbers',
    'Shakespeare wrote 37 plays, 154 sonnets, and invented phrases like "break the ice," "wild goose chase," and "heart of gold." His plays have been translated into every major language and performed more than the combined total of every modern movie script!')

# Broadway Tower
pdf.add_page()
pdf.chapter_title('Broadway Tower - A Folly with a View')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "This 65-foot tower sits on the second-highest point of the Cotswolds at 1,024 feet. It was built in 1798 by Capability Brown. From the top, you can see 16 counties on a clear day!")

pdf.fact_box('B', 'The Cold War Bunker',
    'During the Cold War, a nuclear bunker was built inside Broadway Hill. A team of observers would have climbed into this tiny bunker to measure radiation levels if nuclear war broke out. They had enough food and water for 3 weeks. The bunker is now a museum.')

# Castle Combe
pdf.add_page()
pdf.chapter_title('Castle Combe - The Prettiest Village')
pdf.set_font("DejaVu", '', 9)
pdf.set_text_color(27, 42, 74)
pdf.multi_cell(170, 5, "Often called the prettiest village in England. It has no traffic lights, no street lamps (gas lamps instead), and looks exactly like a medieval village. The market cross in the center has stood there since the 14th century.")

pdf.fact_box('F', 'Movie Star Village',
    'Castle Combe has been the backdrop for countless movies including Dr. Dolittle (1967), The Wolfman, and the TV series Poldark. The village council charges film crews and uses the money to maintain the ancient buildings.')

# Quick facts
pdf.add_page()
pdf.chapter_title('Quick-Fire Fun Facts')
pdf.ln(2)

quick_facts = [
    ('Brighton Beach', 'Covered in millions of pebbles, not sand. The waves make a shingle music sound.'),
    ('Brighton Palace Pier', '1,760 feet long. Middle section removed during WWII to stop enemy boats.'),
    ('Royal Pavilion', 'King George IV built it - looks Indian outside, Chinese inside. Just because he could.'),
    ('Oxford University', 'Over 900 years old. Older than the Aztec Empire. Older than the printing press.'),
    ('Bodleian Library', '13 million books across 80 miles of shelves.'),
    ('Arlington Row', 'Built 1380 as a wool store. On every UK passport.'),
    ('St Edward Church', 'Mentioned in the Domesday Book (1086). North door looks like Doors of Durin.'),
    ("Clarkson Farm", 'Jeremy Clarkson had no idea what he was doing. Farming is HARD.'),
    ('Shakespeare', 'Born 1564. Invented 1,700+ words. Classroom still exists.'),
    ('Broadway Tower', '65-foot tower at 1,024 feet elevation. Cold War bunker inside.'),
    ('Castle Combe', 'Prettiest village in England. No traffic lights. Film sets love it.'),
]

for title, fact in quick_facts:
    pdf.set_font("DejaVu", 'B', 9)
    pdf.set_text_color(27, 42, 74)
    pdf.cell(55, 5, title)
    pdf.set_font("DejaVu", '', 8)
    pdf.set_text_color(90, 103, 120)
    pdf.multi_cell(115, 5, fact)
    pdf.ln(1)

path = '/opt/data/wanderlit-kids/sample-books/brighton-cotswolds-adventure.pdf'
os.makedirs('/opt/data/wanderlit-kids/sample-books', exist_ok=True)
pdf.output(path)
print(f'PDF saved: {path}')
print(f'Pages: {pdf.page_no()}')
print(f'Size: {os.path.getsize(path)} bytes')