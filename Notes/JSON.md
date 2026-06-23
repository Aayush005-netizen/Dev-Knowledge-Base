# 🗂️ JSON — Beginner to Expert

> **Source:** Learn Code With Durgesh — JSON Beginner to Expert Level Tutorial (Hindi)  
> **Standard:** RFC 8259 / ECMA-404 | Created by Douglas Crockford (early 2000s)

---

## Table of Contents

- [What is JSON?](#what-is-json)
- [JSON vs XML](#json-vs-xml)
- [JSON Syntax Rules](#json-syntax-rules)
- [Data Types](#data-types)
- [JSON Object](#json-object)
- [JSON Array](#json-array)
- [Nested JSON](#nested-json)
- [JSON in JavaScript](#json-in-javascript)
  - [JSON.parse()](#jsonparse)
  - [JSON.stringify()](#jsonstringify)
- [JSON in Python](#json-in-python)
- [JSON in Java](#json-in-java)
- [JSON Schema & Validation](#json-schema--validation)
- [Common Mistakes](#common-mistakes)
- [Security Considerations](#security-considerations)
- [Real-World Use Cases](#real-world-use-cases)
- [Quick Reference](#quick-reference)
- [Interview Q&A](#interview-qa)

---

## What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight, text-based, language-independent data interchange format.

- Derived from JavaScript but works with **every major language**
- Primary use: transfer data between a **server and a client**
- Human-readable and machine-parseable
- Standardized in **RFC 8259** and **ECMA-404**

```json
{
  "name": "Aayush",
  "age": 21,
  "isStudent": true,
  "skills": ["Python", "C++", "Flask"],
  "address": {
    "city": "Delhi",
    "country": "India"
  }
}
```

---

## JSON vs XML

| Feature | JSON | XML |
|---|---|---|
| Verbosity | Minimal — no closing tags | Verbose — every tag has open/close |
| Readability | Easy to read | Harder to read |
| Data types | Native support | Everything is text |
| Parsing speed | Faster | Slower |
| Use case | REST APIs, configs, NoSQL | Enterprise, documents, SOAP |
| Array support | Native `[]` | Needs workarounds |
| Comments | ❌ Not supported | ✅ Supported |

**JSON:**
```json
{ "name": "Aayush", "age": 21 }
```

**Same in XML:**
```xml
<person>
  <name>Aayush</name>
  <age>21</age>
</person>
```

> JSON wins for APIs. XML still used in enterprise systems and SOAP services.

---

## JSON Syntax Rules

1. Data is in **key/value pairs**
2. Keys must be **strings in double quotes** (`"key"`)
3. Values must be a valid JSON data type
4. Key-value pairs separated by **comma** (`,`)
5. Objects wrapped in **curly braces** `{}`
6. Arrays wrapped in **square brackets** `[]`
7. **No trailing commas** allowed
8. **No comments** allowed
9. **No single quotes** — always double quotes

```json
// ❌ INVALID JSON
{
  name: "Aayush",        // key not in quotes
  'age': 21,             // single quotes
  "city": "Delhi",       // trailing comma not allowed at end
}

// ✅ VALID JSON
{
  "name": "Aayush",
  "age": 21,
  "city": "Delhi"
}
```

---

## Data Types

JSON supports exactly **6 data types**:

| Type | Example | Notes |
|---|---|---|
| **String** | `"Hello"` | Must use double quotes |
| **Number** | `42`, `3.14`, `-7` | No int vs float distinction |
| **Boolean** | `true`, `false` | Lowercase only |
| **Null** | `null` | Represents absence of value |
| **Object** | `{ "key": "value" }` | Unordered key-value pairs |
| **Array** | `[1, 2, 3]` | Ordered list of values |

```json
{
  "username": "aayush005",
  "score": 98.5,
  "isPremium": false,
  "lastLogin": null,
  "tags": ["dev", "student", "dsa"],
  "profile": {
    "city": "Delhi",
    "github": "Aayush005-netizen"
  }
}
```

> ⚠️ **Important:** `null` ≠ empty string `""`. A missing field and a `null` field are technically different things.

---

## JSON Object

An **object** is an **unordered** collection of key-value pairs inside `{}`.

```json
{
  "id": 1,
  "name": "Mango Lassi",
  "price": 80.0,
  "available": true,
  "category": null
}
```

- Keys → always strings in double quotes
- Values → any valid JSON type
- Access in JavaScript: `obj.name` or `obj["name"]`

---

## JSON Array

An **array** is an **ordered** list of values inside `[]`.

```json
["Python", "C++", "JavaScript", "Flask"]
```

Arrays can hold **mixed types**:

```json
[42, "hello", true, null, { "key": "value" }, [1, 2, 3]]
```

Array of objects (most common in APIs):

```json
[
  { "id": 1, "name": "Aayush", "role": "dev" },
  { "id": 2, "name": "Nikhil", "role": "dev" },
  { "id": 3, "name": "Laiba",  "role": "designer" }
]
```

---

## Nested JSON

JSON objects and arrays can be nested to any depth:

```json
{
  "team": "SANKALP",
  "project": "NEEV",
  "members": [
    {
      "name": "Aayush",
      "role": "Voice & Skill Extraction",
      "skills": ["Python", "Flask", "NLP"],
      "contact": {
        "email": "aayushofficial2005@gmail.com",
        "github": "Aayush005-netizen"
      }
    },
    {
      "name": "Nikhil",
      "role": "Credential & Verification",
      "skills": ["React", "Node.js"]
    }
  ],
  "hackathon": {
    "name": "Build for Good 2026",
    "theme": "ROZGAAR",
    "status": "active"
  }
}
```

---

## JSON in JavaScript

### JSON.parse()

Converts a **JSON string → JavaScript object**.

```javascript
const jsonString = '{"name": "Aayush", "age": 21, "isStudent": true}';

const obj = JSON.parse(jsonString);

console.log(obj.name);      // "Aayush"
console.log(obj.age);       // 21
console.log(obj.isStudent); // true
```

**Always wrap in try/catch — invalid JSON throws SyntaxError:**

```javascript
try {
  const data = JSON.parse(userInput);
  console.log(data);
} catch (e) {
  console.error("Invalid JSON:", e.message);
}
```

---

### JSON.stringify()

Converts a **JavaScript object → JSON string**.

```javascript
const user = {
  name: "Aayush",
  age: 21,
  skills: ["Python", "C++"]
};

// Basic
const jsonStr = JSON.stringify(user);
// '{"name":"Aayush","age":21,"skills":["Python","C++"]}'

// Pretty print (3rd argument = indent spaces)
const pretty = JSON.stringify(user, null, 2);
/*
{
  "name": "Aayush",
  "age": 21,
  "skills": [
    "Python",
    "C++"
  ]
}
*/
```

**Filter specific keys (replacer array):**

```javascript
JSON.stringify(user, ["name", "age"], 2);
// Only includes name and age
```

> ⚠️ `undefined`, functions, and `Symbol` values are **dropped** by `JSON.stringify()`.

---

## JSON in Python

Python's built-in `json` module handles JSON natively.

```python
import json

# Python dict → JSON string (serialize)
data = {
    "name": "Aayush",
    "age": 21,
    "skills": ["Python", "Flask"],
    "active": True,   # Python True → JSON true
    "score": None     # Python None → JSON null
}

json_string = json.dumps(data)
print(json_string)
# '{"name": "Aayush", "age": 21, "skills": ["Python", "Flask"], "active": true, "score": null}'

# Pretty print
pretty = json.dumps(data, indent=2)

# JSON string → Python dict (deserialize)
parsed = json.loads(json_string)
print(parsed["name"])  # "Aayush"

# Read JSON from file
with open("data.json", "r") as f:
    file_data = json.load(f)

# Write JSON to file
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
```

**Python ↔ JSON Type Mapping:**

| Python | JSON |
|---|---|
| `dict` | Object `{}` |
| `list`, `tuple` | Array `[]` |
| `str` | String |
| `int`, `float` | Number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

---

## JSON in Java

Using the popular **Jackson** library:

```java
// Add to pom.xml
// <dependency>
//   <groupId>com.fasterxml.jackson.core</groupId>
//   <artifactId>jackson-databind</artifactId>
// </dependency>

import com.fasterxml.jackson.databind.ObjectMapper;

ObjectMapper mapper = new ObjectMapper();

// Java object → JSON string
String json = mapper.writeValueAsString(userObject);

// JSON string → Java object
User user = mapper.readValue(jsonString, User.class);

// JSON string → Map (when no class available)
Map<String, Object> map = mapper.readValue(jsonString, Map.class);
```

---

## JSON Schema & Validation

**JSON Schema** is a vocabulary for describing and validating the structure of JSON data. Think of it like TypeScript interfaces, but for JSON.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://example.com/user.schema.json",
  "title": "User",
  "description": "A user of the application",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "Unique identifier"
    },
    "name": {
      "type": "string",
      "minLength": 2,
      "maxLength": 100
    },
    "email": {
      "type": "string",
      "format": "email"
    },
    "age": {
      "type": "integer",
      "minimum": 0,
      "maximum": 120
    },
    "role": {
      "type": "string",
      "enum": ["admin", "user", "guest"]
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    }
  },
  "required": ["id", "name", "email"]
}
```

**Validation in Python:**

```python
import jsonschema
import json

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age":  {"type": "integer", "minimum": 0}
    },
    "required": ["name"]
}

data = {"name": "Aayush", "age": 21}

try:
    jsonschema.validate(instance=data, schema=schema)
    print("Valid!")
except jsonschema.ValidationError as e:
    print("Invalid:", e.message)
```

**Common Schema Keywords:**

| Keyword | Purpose |
|---|---|
| `type` | Data type constraint |
| `required` | Array of mandatory keys |
| `properties` | Define object fields |
| `minLength` / `maxLength` | String length bounds |
| `minimum` / `maximum` | Number range |
| `enum` | Allowed values list |
| `pattern` | Regex constraint on string |
| `format` | Semantic format (`email`, `date`, `uuid`) |
| `items` | Schema for array elements |
| `$ref` | Reference another schema |

---

## Common Mistakes

```json
// ❌ Single quotes on keys or values
{ 'name': 'Aayush' }

// ❌ Unquoted keys
{ name: "Aayush" }

// ❌ Trailing comma
{ "name": "Aayush", "age": 21, }

// ❌ Comments (not valid in JSON)
{ "name": "Aayush" /* user name */ }

// ❌ undefined as a value (JavaScript-only concept)
{ "val": undefined }

// ✅ All correct
{
  "name": "Aayush",
  "age": 21,
  "active": true,
  "score": null
}
```

---

## Security Considerations

| Risk | Fix |
|---|---|
| **Prototype pollution (JS)** | Use `Object.create(null)` or sanitize keys like `__proto__` |
| **Large payload DoS** | Set max `Content-Length` on API — a few MB is reasonable |
| **Number precision** | Integers > 2^53 lose precision — use strings for large IDs (Twitter snowflake IDs) |
| **Untrusted input** | Always validate against JSON Schema before processing |
| **Deeply nested JSON** | Can cause stack overflows in parsers — set depth limits |

```javascript
// ⚠️ Dangerous — prototype pollution
const data = JSON.parse('{"__proto__": {"isAdmin": true}}');

// ✅ Safer pattern
const safe = Object.assign(Object.create(null), JSON.parse(input));
```

---

## Real-World Use Cases

| Use Case | Example |
|---|---|
| **REST APIs** | Every API response — `Content-Type: application/json` |
| **Config files** | `package.json`, `tsconfig.json`, `settings.json` |
| **NoSQL Databases** | MongoDB stores BSON (Binary JSON) |
| **Message Queues** | Kafka, RabbitMQ — event payloads in JSON |
| **Microservices** | Inter-service communication format |
| **Frontend State** | `localStorage`, Redux state, API caching |

---

## Quick Reference

| Operation | JavaScript | Python |
|---|---|---|
| Parse string → object | `JSON.parse(str)` | `json.loads(str)` |
| Object → JSON string | `JSON.stringify(obj)` | `json.dumps(obj)` |
| Pretty print | `JSON.stringify(obj, null, 2)` | `json.dumps(obj, indent=2)` |
| Read from file | — | `json.load(file)` |
| Write to file | — | `json.dump(obj, file)` |
| Validate schema | `ajv` library | `jsonschema` library |

---

## Interview Q&A

**Q: What is JSON and why is it used?**  
JSON is a lightweight, text-based data interchange format used to transfer structured data between a server and a client. It's language-independent, human-readable, and maps directly to data structures in most programming languages, making it the default format for REST APIs.

---

**Q: What are the 6 JSON data types?**  
String, Number, Boolean, Null, Object, Array.

---

**Q: What is the difference between `JSON.parse()` and `JSON.stringify()`?**  
`JSON.parse()` converts a JSON string into a JavaScript object (deserialization). `JSON.stringify()` converts a JavaScript object into a JSON string (serialization).

---

**Q: Why doesn't JSON support comments?**  
JSON was designed as a pure data format, not a configuration format. Comments were intentionally excluded to keep parsing simple and fast. If you need comments in config files, use YAML or JSON5.

---

**Q: What happens to `undefined` and functions in `JSON.stringify()`?**  
They are silently dropped. `{ "fn": () => {} }` becomes `{}` after stringification.

---

**Q: What is JSON Schema?**  
JSON Schema is a vocabulary for describing and validating the structure of JSON data. It acts as a contract between API producers and consumers — defining required fields, data types, allowed values, and constraints.

---

**Q: What is the difference between `null` and a missing field in JSON?**  
A field set to `null` explicitly communicates absence of a value. A missing field means the key was never included. They're technically different and parsers may handle them differently.

---

**Q: JSON vs XML — when would you choose XML?**  
XML for: enterprise systems, SOAP services, documents with complex namespaces, when comments and attributes matter. JSON for: REST APIs, web apps, mobile apps, NoSQL databases — anywhere speed and simplicity matter.

---

**Q: What is `None` in Python when converting to JSON?**  
Python's `None` maps to JSON's `null`. Similarly, `True`/`False` maps to `true`/`false`.

---

**Q: How do you handle large IDs (like Twitter's) in JSON?**  
JSON numbers are IEEE 754 doubles, which can't precisely represent integers > 2^53. For large IDs, always serialize them as **strings** to avoid precision loss.

---

*Last updated: June 2026*