

# Tamil stopwords
tamil_stopwords = [
    "ஒன்று",
    "மற்றும்","அது","அதிகம்","எல்லாம்","வேண்டும்","அவர்கள்","இப்படி","என்று","இல்லை","மூலம்",
    "இன்று","மாற்றம்","போய்விட்டது","இங்கு","இது","தன்னுடைய","மீதம் உள்ளது","ஆண்டு","மிகவும்",
    "நான்","என்ன","நடந்துள்ளது","தன்","எங்கு","அந்த","என்","மறுபடியும்","இதே","பிடித்தல்","முதல்",
    "அல்ல","அல்லது","ஏன்","பெற்றுள்ளது","பெற்ற","செய்த","நடக்கும்","மற்றவர்கள்","வரும்","அது",
    "சிறப்பு","சிறிய","எதிரான","எதிராக","சில","மேலே","யார்","நாள்","நேரம்","ஒன்றரை","பரிசு",
    "உள்ளது","நாளை","வரும்","காரணமாக","உடனடி","சிறந்த","நடக்கும்","எதிராக","தொடங்கியது",
    "புதிய","இருந்தது","அதை","ஒன்றில்","தொடர்பான","தொடர்புடைய","மேலே",
]


Additional_Aspects_Filter_tamil = [
    # Bad and synonyms
    "உங்க " # yours
    "பெரிய",
    "நல்ல",#Good
    "சரியில்லை",#not good
    "நன்றாக",#good
    "இருக்கிறது",#There
    "நல்லா",#Good
    "இருக்கு",#there
    "கெட்ட",  # ಕೆಟ್ಟ (Ketta) - 
    "கெட்டது",  # ಕೆಟ್ಟತು (Kettatu) - 
    "கெட்டவை",  # ಕೆಟ್ಟವೈ (Kettavai) - 
    "கெட்டதுதான்",  # ಕೆಟ್ಟತುತಾನ್ (Kettatutaan) - 
    "கெட்டதாக",  # ಕೆಟ್ಟತುವಾಗ (Kettatuvaaga) - 
    "கெட்டதே",  # ಕೆಟ್ಟತುವೇ (Kettatuve) - 
    "கெட்டதும்",  # ಕೆಟ್ಟತುಮ್ (Kettatum) - 
    "ஏழை",  # Poor (Yezhai) - 
    "கெட்டதாகியது",  # ಕೆಟ್ಟದಾಗಿದೆ (Kettadaagide) - 
    "கெட்டதல்ல",  # Not Bad (Kettatalla) - 
    "கெட்டதல்லது",  # Not Bad (Kettatallatu) - 
    "கெட்டதல்லவை",  # Not Bad (Kettatallavai) - 
    "கெட்டதல்லதுதான்",  # Not Bad (Kettatallatutaan) - 
    "ಕೆಟ್ಟತಲ್ಲತುವಾಗ",  # Not Bad (Kettatallatuvaaga) - 
    "கெட்டதல்லதாக",  # Not Bad (Kettatallatuve) - கெட்டதல்லதே
    "கெட்டதல்லதும்",  # Not Bad (Kettatallatum) - 
    "கெட்டதல்லிருக்கு",  # Not Bad (Kettatallirukku) - 
    "கெட்டதல்லிருக்கிருக்கு",  # Not Bad (Kettatallirukkirukku) - 
    "ஓகே",  # OK (Oke) - 
    "குணநிலையை",  # Behaviour (Gunamattavannu) - 
    "ஆனால்",  # But (Aadare) - 
    "சிறிது",  # Little (Swalpa) - 
    "பெரிதாகியுள்ளது",  # Huge (Hechchaagide) - 
    "மோசமாக",# worst

    # Great and synonyms
    "நல்லது",  # Good (Olleyadu) - 
    "மிகவும் நல்ல",  # Great (Mikavum Nalla) - 
    "மிகவும் நல்லது",  # Excellent (Mikavum Nallatu) - 
    "மிகவும் நல்லவை",  # Superb (Mikavum Nallavai) - 
    "மிகவும் நல்லதுதான்",  # Outstanding (Mikavum Nallatutaan) - 
    "மிகவும் நல்லதாக",  # Remarkable (Mikavum Nallatuvaaga) - 
    "மிகவும் நல்லதே",  # Splendid (Mikavum Nallatuve) - 
    "மிகவும் நல்லதும்",  # Great (Mikavum Nallatum) - 
    "மிகவும் நல்லதல்ல",  # Not Great (Mikavum Nallatalla) - 
    "மிகவும் நல்லதல்லது",  # Not Great (Mikavum Nallatallatu) - 
    "மிகவும் நல்லதல்லவை",  # Not Great (Mikavum Nallatallavai) - 
    "மிகவும் நல்லதல்லதுதான்",  # Not Great (Mikavum Nallatallatutaan) - 
    "மிகவும் நல்லதல்லதாக",  # Not Great (Mikavum Nallatallatuvaaga) - 
    "மிகவும் நல்லதல்லதே",  # Not Great (Mikavum Nallatallatuve) - 
    "மிகவும் நல்லதல்லதும்",  # Not Great (Mikavum Nallatallatum) - 
    "மிகவும் நல்லதல்லிருக்கு",  # Not Great (Mikavum Nallatallirukku) - 
    "மிகவும் நல்லதல்லிருக்கிருக்கு",  # Not Great (Mikavum Nallatallirukkirukku) - 

    # Awesome and synonyms
    "அருமை",  # Awesome (Arputam) - 
    "அருமையான",  # Amazing (Arputamaan) - 
    "அருமையாக",  # Astonishing (Arputamaaga) - 
    "அருமையான",  # Astounding (Arputamaaya) - 
    "அருமையாக இருக்கும்",  # Breathtaking (Arputamaayirukkum) - 
    "அருமையாக இருக்க இருக்கு",  # Incredible (Arputamaayirukkirukku) - 
    "அருமையாக இருக்கும்",  # Marvelous (Arputamaayirukku) -  
    "அருமையானதல்ல",  # Not Awesome (Arputamaayatalla) - 
    "அருமையானதல்லது",  # Not Awesome (Arputamaayatallatu) - 
    "அருமையானதல்லவை",  # Not Awesome (Arputamaayatallavai) - 
    "அருமையானதல்லதுதான்",  # Not Awesome (Arputamaayatallatutaan) - 
    "அருமையானதல்லதாக",  # Not Awesome (Arputamaayatallatuvaaga) - 
    "அருமையானதல்லதே",  # Not Awesome (Arputamaayatallatuve) - 
    "அருமையானதல்லதும்",  # Not Awesome (Arputamaayatallatum) - 
    "அருமையானதல்லிருக்கு",  # Not Awesome (Arputamaayatallirukku) - 
    "அருமையானதல்லிருக்கிருக்கு",  # Not Awesome (Arputamaayatallirukkirukku) - 

    # Worst and synonyms
    "மேலான",  # Worst (Melana) - 
    "மேலானது",  # Worst (Melanatu) - 
    "மேலானவை",  # Worst (Melanavai) - 
    "மேலானதுதான்",  # Worst (Melanatuthaan) - 
    "மேலானதாக",  # Inferior (Melanatuvaaga) - 
    "மேலானதே",  # Poor (Melanatuve) - 
    "மேலானதும்",  # Worst (Melanatum) - 
    "மோசமான",  # Worst (Moshamaana) - 
    "மோசமானது",  # Worst (Moshamaanatu) - 
    "நல்லதல்ல",  # Not Worst (Nallatalla) - 
    "நல்லதல்லது",  # Not Worst (Nallatallatu) - 
    "நல்லதல்லவை",  # Not Worst (Nallatallavai) - 
    "நல்லதல்லதுதான்",  # Not Worst (Nallatallatutaan) - 
    "நல்லதல்லதாக",  # Not Worst (Nallatallatuvaaga) - 
    "நல்லதல்லதே",  # Not Worst (Nallatallatuve) - 
    "நல்லதல்லதும்",  # Not Worst (Nallatallatum) - 
    "நல்லதல்லிருக்கு",  # Not Worst (Nallatallirukku) - 
    "நல்லதல்லிருக்கிருக்கு",  # Not Worst (Nallatallirukkirukku) - 
    "கெட்டதாகியது",  # Worst (Kettadaagide) - 

    # Irrelevant
    "என்னை",  # Me (Ennai) - 
    "எனது",  # Me (Enatu) - 
    "நான்",  # Me (Naan) - 
    "அதிர்ச்சியில்",  # In shock (Athirchiyil) - 
    "ஆழ்வை",  # Depth (Aazhaik) - 
    "கொண்டுள்ளது",  # Contains (Kontullatu) - 
    "வாழ்க்கையை",  # Life (Vaazhkaiyai) - 
    "எளிதாக்கியுள்ளது",  # Made Easy (Elitakkiyullatu) - 
    "அனைவருக்கும்",  # For Everyone (Anaivarukkum) - 
    "பரிந்துரைக்கின்",  # I Recommend (Parinthuraikkin) - 
]

kannada_stopwords = [
    "ಒಂದು", "ಮತ್ತು", "ಅದು", "ಹೆಚ್ಚು", "ಎಲ್ಲವೂ", "ಬೇಕು", "ಅವರು", "ಹೀಗೆ",
    "ಎಂದು", "ಇಲ್ಲ", "ಮೂಲಕ", "ಎಂದು", "ಇಂದು", "ಬದಲಾವಣೆ", "ಹೋಗಿದೆ", "ಇಲ್ಲಿ",
    "ಈ", "ಎಂದು", "ತನದು", "ಉಳಿದಿದೆ", "ವರ್ಷ", "ಅತ್ಯಂತ", "ಅಲ್ಲ", "ಹೆಚ್ಚು", "ನಾನು",
    "ಎಂದು", "ಏನು", "ಅದು", "ಆಗಿದೆ", "ತನ", "ಎಲ್ಲಿಯೂ", "ಹೀಗೆ", "ಇದು",
    "ಆ", "ನನ್ನ", "ಆಗಿದೆ", "ಮತ್ತೆ", "ಅವರು", "ಇದೇ", "ಹಿಡಿತ", "ಮೊದಲ",
    "ಅಲ್ಲಾ", "ಅಥವಾ", "ಏಕೆ", "ಹೊಂದಿದೆ", "ಮೊದಲ", "ಪಡೆದ", "ಮಾಡಿದ", "ನಡೆಯುವ",
    "ಅನ್ನಿತರ", "ಬರುತ್ತದೆ", "ಒಂದೇ", "ಅದರ", "ಎಂದು", "ವಿಶೇಷ", "ಸಣ್ಣ", "ಎದುರಾದ",
    "ಎದುರಾಗಿ", "ಕೆಲವು", "ಮೇಲೆ", "ಯಾರು", "ದಿನ", "ಹೊತ್ತು", "ಒಂದುವರೆ", "ಅತ್ಯಂತ",
    "ಬಹುಮಾನ", "ಇರುವುದು", "ನಾಳೆ", "ಬರುವ", "ಕಾರಣವಾಗಿ", "ತಕ್ಷಣದ", "ಶ್ರೇಷ್ಠ", "ಹೆಚ್ಚು",
    "ನಡೆದ", "ವಿರುದ್ಧ", "ಪ್ರಾರಂಭವಾಯಿತು", "ವಿರುದ್ಧ", "ಹೊಸ", "ಆಗಿದ್ದ", "ಅದನ್ನು", "ಒಂದಲ್ಲಿ",
    "ಬರುವ", "ಸಂಬಂಧದ", "ಸಂಬಂಧಿತ", "ಮೇಲೆ",
]
Additional_Aspects_Filter_kannada = [
# Bad and synonyms
"ಕೆಟ್ಟ",  # Bad
"ಕೆಟ್ಟತು",  # Bad
"ಕೆಟ್ಟವೈ",  # Bad
"ಕೆಟ್ಟತುತಾನ್",  # Bad
"ಕೆಟ್ಟತುವಾಗ",  # Poor
"ಕೆಟ್ಟತುವೇ",  # Inferior
"ಕೆಟ್ಟತುಮ್",  # Bad
"ಸ್ವತಃ",# Correct
"ಏಳೈ",#Poor
"ಉತ್ತಮ",#Good
"ಕೆಟ್ಟದಾಗಿದೆ",#Bad
"ಕೆಟ್ಟತಲ್ಲ",#Not Bad
"ಕೆಟ್ಟತಲ್ಲತು",#Not Bad
"ಕೆಟ್ಟತಲ್ಲವೈ",#Not Bad
"ಕೆಟ್ಟತಲ್ಲತುತಾನ್",#Not Bad
"ಕೆಟ್ಟತಲ್ಲತುವಾಗ",#Not Bad
"ಕೆಟ್ಟತಲ್ಲತುವೇ",#Not Bad
"ಕೆಟ್ಟತಲ್ಲತುಮ್",#Not Bad
"ಕೆಟ್ಟತಲ್ಲಿರುಕ್ಕು",#Not Bad
"ಕೆಟ್ಟತಲ್ಲಿರುಕ್ಕಿರುಕ್ಕು",#Not Bad
"ಓಕೆ",#ok
"ಗುಣಮಟ್ಟವನ್ನು",#behaviour
"ಆದರೆ",#but
"ಸ್ವಲ್ಪ",#little
"ಹೆಚ್ಚಾಗಿದೆ",#huge

# Great and synonyms
"ಒಳ್ಳೆಯದು",#good
"ಮಿಕವುಮ್ ನಲ್ಲ",  # Great
"ಮಿಕವುಮ್ ನಲ್ಲತು",  # Excellent
"ಮಿಕವುಮ್ ನಲ್ಲವೈ",  # Superb
"ಮಿಕವುಮ್ ನಲ್ಲತುತಾನ್",  # Outstanding
"ಮಿಕವುಮ್ ನಲ್ಲತುವಾಗ",  # Remarkable
"ಮಿಕವುಮ್ ನಲ್ಲತುವೇ",  # Splendid
"ಮಿಕವುಮ್ ನಲ್ಲತುಮ್",  # Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲ",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲತು",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲವೈ",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲತುತಾನ್",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲತುವಾಗ",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲತುವೇ",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲತುಮ್",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲಿರುಕ್ಕು",#Not Great
"ಮಿಕವುಮ್ ನಲ್ಲತಲ್ಲಿರುಕ್ಕಿರುಕ್ಕು",#Not Great

# Awesome and synonyms
"ಅಱ್ಪುತಮ್",  # Awesome
"ಅಱ್ಪುತಮಾನ",  # Amazing
"ಅಱ್ಪುತಮಾಗ",  # Astonishing
"ಅಱ್ಪುತಮಾಯ",  # Astounding
"ಅಱ್ಪುತಮಾಯಿರುಕ್ಕುಮ್",  # Breathtaking
"ಅಱ್ಪುತಮಾಯಿರುಕ್ಕಿರುಕ್ಕು",  # Incredible
"ಅಱ್ಪುತಮಾಯಿರುಕ್ಕು",  # Marvelous
"ಅಱ್ಪುತಮಾಯತಲ್ಲ",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲತು",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲವೈ",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲತುತಾನ್",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲತುವಾಗ",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲತುವೇ",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲತುಮ್",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲಿರುಕ್ಕು",#Not Awesome
"ಅಱ್ಪುತಮಾಯತಲ್ಲಿರುಕ್ಕಿರುಕ್ಕು",#Not Awesome

# Worst and synonyms
"ಮೇಲಾನ",  # Worst
"ಮೇಲಾನತು",  # Worst
"ಮೇಲಾನವೈ",  # Worst
"ಮೇಲಾನತುತಾನ್",  # Worst
"ಮೇಲಾನತುವಾಗ",  # Inferior
"ಮೇಲಾನತುವೇ",  # Poor
"ಮೇಲಾನತುಮ್",  # Worst
"ಮೋಷಮಾನ", #Worst
"ಮೋಷಮಾನತು"#Worst
"ನಲ್ಲತಲ್ಲ",#Not Worst
"ನಲ್ಲತಲ್ಲತು",#Not Worst
"ನಲ್ಲತಲ್ಲವೈ",#Not Worst
"ನಲ್ಲತಲ್ಲತುತಾನ್",#Not Worst
"ನಲ್ಲತಲ್ಲತುವಾಗ",#Not Worst
"ನಲ್ಲತಲ್ಲತುವೇ",#Not Worst
"ನಲ್ಲತಲ್ಲತುಮ್",#Not Worst
"ನಲ್ಲತಲ್ಲಿರುಕ್ಕು",#Not Worst
"ನಲ್ಲತಲ್ಲಿರುಕ್ಕಿರುಕ್ಕು",#Not Worst
"ಕೆಟ್ಟದಾಗಿದೆ",#worst

# Irrelevant
"ಎನ್ನೈ", #Me
"ಎನತು",#Me
"ನಾನ್",#me
"ಅತಿರ್ಚ್ಚಿಯಿಲ್", # In shock
"ಆ಴್ವೈಕ್",#Depth
"ಕೊಣ್ಟುಳ್ಳತು",#Contains
"ವಾ಴್ಕೈಯೈ",#life
"ಎಳಿತಾಕ್ಕಿಯುಳ್ಳತು",#made Easy
"ಅನೈವರುಕ್ಕುಮ್",#For Everyone
"ಪರಿನ್ತುರೈಕ್ಕಿನ್",#i Recommend
]