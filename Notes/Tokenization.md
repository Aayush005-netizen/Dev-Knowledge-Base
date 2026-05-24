# 🔤 Tokenization — LLM from Scratch (Vizuara Lecture 7)

> **Course:** Build an LLM from Scratch — Vizuara  
> **Lecture:** 7 — Code an LLM Tokenizer from Scratch in Python  
> **Reference Book:** *Build a Large Language Model from Scratch* — Manning Publications  
> **Duration:** 1:09:44  
> **Video:** [Watch on YouTube](https://www.youtube.com/watch?v=rsy5Ragmso8)

---

## 📌 Lecture Goals

Is lecture mein hum ek simple tokenizer banayenge **from scratch in Python**. Yeh samjhenge:

- Tokenization kya hota hai aur LLMs ko kyun chahiye
- Text ko tokens mein convert karna
- Tokens ko Token IDs mein convert karna
- Ek proper `SimpleTokenizer` Python class banana
- Special/context tokens ka use

---

## 1️⃣ What is Tokenization?

Tokenization = **Text (string) → Numbers (integers)** ka conversion process.

LLMs sirf numbers samajhte hain, isliye hume raw text ko pehle numbers mein todna padta hai. Yeh numbers hi model ke input hote hain.

**Example:**
```
"Hello, world!"  →  [9906, 11, 1917, 0]
```

Yeh numbers (token IDs) model ke **embedding layer** mein jaate hain.

---

## 2️⃣ Two Steps of Tokenization

Tokenization 2 steps mein hoti hai:

**Step 1: Text → Tokens**  
Raw text ko chhote pieces (tokens) mein todna. Yeh pieces words, subwords, ya characters ho sakte hain.

**Step 2: Tokens → Token IDs**  
Har token ko ek unique integer (ID) se map karna using a **vocabulary** (vocab).

---

## 3️⃣ Importing the Dataset

Is lecture mein **Edith Wharton ki short story "The Verdict"** ko dataset ki tarah use kiya gaya hai (public domain text).

```python
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("Total characters:", len(raw_text))
print(raw_text[:100])  # pehle 100 characters dekho
```

> **Why this text?** Small, clean, English text — tokenizer experiment ke liye perfect.

---

## 4️⃣ Tokenizing the Text

### ❌ Naive Approach — Simple Split

```python
tokens = raw_text.split()
print(tokens[:10])
```

**Problem:** `"Hello,"` aur `"Hello"` alag treat hote hain. Punctuation alag nahi hoti.

---

### ✅ Better Approach — Regex-based Tokenization

```python
import re

tokens = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
tokens = [t.strip() for t in tokens if t.strip()]  # empty strings hatao
print(tokens[:15])
print("Total tokens:", len(tokens))
```

**Regex breakdown:**

| Pattern | Meaning |
|---|---|
| `[,.:;?_!"()\'` | In punctuation marks ko alag token maano |
| `--` | Double dash bhi alag token |
| `\s` | Whitespace pe split karo |
| `.strip()` + `if t.strip()` | Empty tokens filter karo |

**Result:** Har word aur har punctuation mark apna alag token banta hai.

---

## 5️⃣ Converting Tokens → Token IDs

### Vocabulary (Vocab) Banao

Vocabulary = ek dictionary jo har unique token ko ek unique integer se map kare.

```python
# Saare unique tokens collect karo, sort karo
all_words = sorted(set(tokens))
vocab_size = len(all_words)
print("Vocab size:", vocab_size)

# vocab dictionary banao: token → ID
vocab = {token: integer for integer, token in enumerate(all_words)}

# Pehle 10 entries dekho
for token, id in list(vocab.items())[:10]:
    print(f"{token!r:20} → {id}")
```

---

### Encode — Text to IDs

```python
def encode(text):
    tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    tokens = [t.strip() for t in tokens if t.strip()]
    token_ids = [vocab[token] for token in tokens]
    return token_ids

print(encode("Hello, do you like tea?"))
# Output: list of integers
```

---

### Decode — IDs to Text

```python
# Reverse vocab: ID → token
reverse_vocab = {id: token for token, id in vocab.items()}

def decode(token_ids):
    text = " ".join([reverse_vocab[id] for id in token_ids])
    # Punctuation ke pehle extra space hatao
    text = re.sub(r'\s+([,.?!"()\'`])', r'\1', text)
    return text

print(decode(encode("Hello, do you like tea?")))
# Output: "Hello, do you like tea?"
```

---

## 6️⃣ SimpleTokenizer Class in Python

Saari cheez ek clean Python class mein wrap karte hain:

```python
import re

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab                              # token → ID
        self.int_to_str = {v: k for k, v in vocab.items()}  # ID → token

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [t.strip() for t in preprocessed if t.strip()]
        ids = [self.str_to_int[token] for token in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Punctuation fix — extra space hatao
        text = re.sub(r'\s+([,.:;?!"()\'`])', r'\1', text)
        return text
```

**Usage:**

```python
tokenizer = SimpleTokenizerV1(vocab)

text = '"It\'s the last he painted, you know," Mrs. Gisburn said'
ids = tokenizer.encode(text)
print(ids)                    # token IDs
print(tokenizer.decode(ids))  # wapas original text
```

> ⚠️ **Problem with V1:** Agar koi aisa word aaye jo vocab mein nahi hai (unseen word), toh `KeyError` aayega!

---

## 7️⃣ Special / Context Tokens

Real LLMs mein kuch **special tokens** hote hain jo model ko extra context dete hain.

### Common Special Tokens

| Token | Meaning |
|---|---|
| `<\|unk\|>` | Unknown word — jo vocab mein nahi hai |
| `<\|endoftext\|>` | Document ka end mark karta hai |
| `<\|im_start\|>` | Message start (chatbot context) |
| `<\|im_end\|>` | Message end |
| `<\|pad\|>` | Padding token |

---

### Vocab Mein Special Tokens Add Karo

```python
all_tokens = sorted(set(tokens))
all_tokens.extend(["<|unk|>", "<|endoftext|>"])
vocab = {token: integer for integer, token in enumerate(all_tokens)}

print(vocab["<|unk|>"])        # last IDs mein se ek hoga
print(vocab["<|endoftext|>"])
```

---

### SimpleTokenizerV2 — Unknown Words Handle Karta Hai

```python
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {v: k for k, v in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [t.strip() for t in preprocessed if t.strip()]
        # Unknown words ko <|unk|> se replace karo
        preprocessed = [
            t if t in self.str_to_int else "<|unk|>"
            for t in preprocessed
        ]
        ids = [self.str_to_int[t] for t in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.:;?!"()\'`])', r'\1', text)
        return text
```

---

## 8️⃣ `<|endoftext|>` — Multiple Documents Handle Karna

Jab multiple documents ko ek saath train karte hain, unhe `<|endoftext|>` token se separate karte hain. Yeh model ko batata hai:

> **"Ek story khatam, nayi shuru."**

```python
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."

combined = " <|endoftext|> ".join([text1, text2])
print(combined)
# "Hello, do you like tea? <|endoftext|> In the sunlit terraces..."

ids = tokenizer.encode(combined)
print(ids)
print(tokenizer.decode(ids))
```

> **Why important?** Bina is token ke, model ko pata nahi chalega ki documents kahan separate hote hain. Context mix ho jaata.

---

## 9️⃣ Additional Context Tokens & BPE Preview

GPT-2 mein **50,257 token vocabulary** hai, jo in cheez se bani hai:

| Component | Count |
|---|---|
| Base byte tokens | 256 |
| BPE merge tokens | 50,000 |
| Special `<\|endoftext\|>` token | 1 |
| **Total** | **50,257** |

Aage ke lectures mein hum **Byte Pair Encoding (BPE)** seekhenge — yeh wahi algorithm hai jo GPT-2, GPT-4, Llama etc. use karte hain.

**BPE ka core idea:**  
Automatically frequent subword pairs ko merge karta jaata hai jab tak desired vocab size na ho jaaye. Isse model rare/unseen words ko bhi subword chunks ke through handle kar sakta hai.

---

## 🔁 Lecture Recap

| Concept | Summary |
|---|---|
| Tokenization | Text → Tokens → Token IDs |
| Vocab | Unique token ↔ integer mapping |
| `encode()` | Text string → list of IDs |
| `decode()` | List of IDs → text string |
| `SimpleTokenizerV1` | Basic tokenizer, KeyError on unknown words |
| `SimpleTokenizerV2` | Unknown words → `<\|unk\|>` |
| `<\|endoftext\|>` | Documents separate karne ke liye |
| Special Tokens | Model ko extra context dete hain |
| Next Up | Byte Pair Encoding (BPE) |

---

## 💡 Key Takeaways

- LLMs **sirf numbers** process karte hain — isliye tokenization pehla aur zaroori step hai
- Vocabulary ek dictionary hai: **token ↔ integer**
- `encode` aur `decode` inverse operations hain
- Real tokenizers (tiktoken, sentencepiece) BPE use karte hain — simple regex split nahi
- Special tokens jaise `<|endoftext|>` model ke liye critical context provide karte hain
- GPT-2 ka vocab size = **50,257**

---

*Source: Vizuara — Lecture 7 | Build LLM from Scratch*  
*Notes by: Aayush Dubey*
