stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words = [
    "ability", "absolutely", "academic", "accepted", "access", "accident", "according", "account", "accurate", "achieve",
    "acquired", "activity", "actually", "addition", "adequate", "adjustment", "administration", "admission", "admitted", "adult",
    "advance", "advice", "adviser", "advocate", "affect", "afford", "afraid", "agency", "agenda", "agreement",
    "airline", "alliance", "allocate", "almost", "already", "although", "always", "amazing", "American", "amount",
    "analysis", "analyst", "ancient", "anger", "angle", "animal", "annual", "answer", "anxiety", "anybody",
    "apology", "appeal", "appear", "applied", "appoint", "approach", "approval", "argue", "arise", "army",
    "around", "arrange", "arrest", "arrival", "article", "artist", "aspect", "assault", "assert", "assess",
    "assign", "assist", "assume", "assure", "athlete", "attempt", "attend", "attention", "attitude", "attorney",
    "attract", "audience", "author", "authority", "available", "average", "avoid", "award", "aware", "awesome",
    "balance", "barrier", "basically", "battery", "battle", "beauty", "because", "become", "before", "begin",
    "behavior", "belief", "believe", "benefit", "besides", "between", "beyond", "billion", "biology", "birthday",
    "blame", "blessing", "blind", "block", "blood", "board", "bother", "bottle", "bottom", "boundary",
    "breathe", "briefly", "bright", "brilliant", "bring", "brother", "budget", "building", "bullet", "burden",
    "bureau", "business", "button", "buyer", "cabinet", "camera", "campaign", "campus", "cancel", "cancer",
    "candidate", "capacity", "capital", "capture", "carbon", "career", "careful", "carefully", "carrier", "catch",
    "category", "cause", "ceiling", "celebrate", "center", "central", "century", "certain", "certainly", "chain",
    "chair", "challenge", "chamber", "chance", "change", "channel", "chapter", "character", "charge", "charity",
    "chart", "chase", "cheap", "check", "cheese", "chemical", "chief", "choice", "choose", "church",
    "circle", "citizen", "civil", "claim", "class", "classic", "classroom", "clean", "clear", "clearly",
    "client", "climate", "climb", "clinic", "clinical", "clock", "close", "closely", "closer", "clothes",
    "clothing", "cloud", "club", "cluster", "coach", "coal", "coalition", "coast", "coffee", "cognitive",
    "collapse", "colleague", "collect", "college", "colonial", "color", "column", "combine", "come", "comfort",
    "command", "comment", "commercial", "commission", "commit", "commitment", "committee", "common", "communicate", "community",
    "company", "compare", "compete", "competition", "complete", "complex", "complicated", "component", "compose", "comprehensive",
    "computer", "concern", "conclude", "conclusion", "concrete", "condition", "conduct", "conference", "confidence", "confirm",
    "conflict", "confront", "confuse", "connect", "connection", "conscious", "consensus", "consequence", "conservative", "consider",
    "considerable", "consist", "consistent", "constant", "constantly", "constitute", "constitution", "construct", "construction", "consult",
    "consume", "consumer", "contact", "contain", "container", "contemporary", "content", "contest", "context", "continue",
    "contract", "contrast", "contribute", "contribution", "control", "controversy", "convenient", "convention", "conventional", "conversation",
    "convert", "convince", "cookie", "cooking", "cool", "cooperation", "cop", "cope", "copy", "core",
    "corner", "corporate", "corporation", "correct", "correspond", "cost", "cotton", "couch", "could", "council",
    "counsel", "counselor", "count", "counter", "country", "county", "couple", "courage", "course", "court",
    "cousin", "cover", "coverage", "create", "creation", "creative", "creature", "credit", "crew", "crime",
    "criminal", "crisis", "criteria", "critic", "critical", "criticism", "criticize", "crop", "cross", "crowd",
    "crucial", "cruise", "culture", "cup", "curious", "current", "currently", "curriculum", "custom", "customer",
    "cut", "cycle", "daily", "damage", "dance", "danger", "dangerous", "dark", "data", "database",
    "date", "daughter", "day", "dead", "deal", "dealer", "dear", "death", "debate", "debt",
    "decade", "decide", "decision", "declare", "decline", "decrease", "deep", "deeply", "defeat", "defend",
    "defendant", "defense", "defensive", "deficit", "define", "definitely", "definition", "degree", "delay", "deliver",
    "delivery", "demand", "democracy", "Democrat", "democratic", "demonstrate", "demonstration", "denial", "density", "department",
    "departure", "depend", "dependent", "depending", "depict", "deploy", "deposit", "depression", "depth", "deputy",
    "derive", "describe", "description", "desert", "deserve", "design", "designer", "desire", "desk", "desperate",
    "design", "desire", "desktop", "desperate", "despite", "destroy", "detail", "detailed", "detect", "determine",
    "develop", "developer", "development", "device", "devote", "dialogue", "difference", "different", "difficult", "difficulty",
    "digital", "dimension", "dining", "direct", "direction", "directly", "director", "disagree", "disappear", "disaster",
    "discipline", "discourse", "discover", "discovery", "discuss", "discussion", "disease", "dismiss", "disorder", "display",
    "distance", "distinct", "distinction", "distribute", "distribution", "district", "diverse", "diversity", "divide", "division",
    "doctor", "document", "domestic", "dominant", "dominate", "door", "double", "doubt", "down", "downtown",
    "draft", "drama", "dramatic", "drawing", "dream", "dress", "drinking", "drive", "driver", "drop",
    "drug", "during", "duty", "dynamic", "eager", "early", "earn", "earth", "easily", "east",
    "easy", "economic", "economics", "economist", "economy", "edge", "edition", "editor", "educate", "education",
    "educational", "effect", "effective", "effectively", "efficiency", "efficient", "effort", "either", "elderly", "elect",
    "election", "electric", "electricity", "electronic", "element", "elementary", "eliminate", "elite", "else", "elsewhere",
    "embrace", "emerge", "emergency", "emission", "emotion", "emotional", "emphasis", "emphasize", "employ", "employee",
    "employer", "employment", "empty", "enable", "encounter", "encourage", "end", "enemy", "energy", "enforce",
    "engage", "engine", "engineer", "engineering", "English", "enhance", "enjoy", "enormous", "enough", "ensure",
    "enter", "enterprise", "entertainment", "entire", "entirely", "entrance", "entry", "environment", "environmental", "episode",
    "equal", "equally", "equipment", "equity", "equivalent", "error", "escape", "especially", "essay", "essential",
    "essentially", "establish", "establishment", "estate", "estimate", "ethical", "ethics", "ethnic", "European", "evaluate",
    "evaluation", "even", "evening", "event", "eventually", "ever", "every", "everybody", "everyday", "everyone",
    "everything", "everywhere", "evidence", "evolution", "evolve", "exact", "exactly", "examination", "examine", "example",
    "exceed", "excellent", "except", "exception", "exchange", "excite", "exciting", "executive", "exercise", "exhibit",
    "exhibition", "exist", "existence", "existing", "expand", "expansion", "expect", "expectation", "expense", "expensive",
    "experience", "experiment", "expert", "explain", "explanation", "explode", "explore", "explosion", "expose", "exposure",
    "express", "expression", "extend", "extension", "extensive", "extent", "external", "extra", "extraordinary", "extreme",
    "extremely", "eye", "fabric", "face", "facility", "fact", "factor", "factory", "faculty", "fade",
    "fail", "failure", "fair", "fairly", "faith", "fall", "familiar", "family", "famous", "fan",
    "fantasy", "far", "farm", "farmer", "fashion", "fast", "fat", "fate", "father", "fault",
    "favor", "favorite", "fear", "feature", "federal", "fee", "feed", "feel", "feeling", "fellow",
    "female", "fence", "few", "fewer", "field", "fight", "figure", "file", "fill", "film",
    "final", "finally", "finance", "financial", "find", "finding", "fine", "finger", "finish", "fire",
    "firm", "first", "fish", "fishing", "fit", "fitness", "five", "fix", "flag", "flame",
    "flash", "flat", "flavor", "flee", "flesh", "flight", "float", "floor", "flow", "flower",
    "focus", "folk", "follow", "following", "food", "foot", "football", "for", "force", "foreign",
    "forest", "forever", "forget", "form", "formal", "format", "formation", "former", "formula", "forth",
    "fortune", "forward", "found", "foundation", "founder", "four", "fourth", "frame", "framework", "free",
    "freedom", "freeze", "French", "frequency", "frequent", "frequently", "fresh", "friend", "friendly", "friendship",
    "from", "front", "fruit", "frustration", "fuel", "full", "fully", "fun", "function", "fund",
    "fundamental", "funding", "funeral", "funny", "furniture", "further", "furthermore", "future", "gain", "galaxy",
    "gallery", "game", "gang", "gap", "garage", "garden", "gas", "gate", "gather", "gathering",
    "gay", "gaze", "gear", "gender", "gene", "general", "generally", "generate", "generation", "genetic",
    "gentleman", "gently", "German", "gesture", "get", "ghost", "giant", "gift", "gifted", "girl",
    "girlfriend", "give", "given", "glad", "glance", "glass", "global", "glove", "go", "goal",
    "god", "gold", "golden", "golf", "good", "government", "governor", "grab", "grade", "gradually",
    "graduate", "grain", "grand", "grandfather", "grandmother", "grant", "grass", "grave", "great", "greatest",
    "green"]
logo ="""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""