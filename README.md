# Rawyverse 📚

A comprehensive platform for discovering and managing books and novels, featuring a robust authentication system and an optimized API.

**Live Website:** [rawyverse.xyz](https://rawyverse.xyz)
**API:** [api.rawyverse.xyz](https://api.rawyverse.xyz)

---

## 📝 A Note on This Project (My Learning Journey)
This is quite literally my **very first software project**. Instead of practicing with isolated coding exercises, I decided to dive in and build a full, real-world application to apply everything I learn along the way. 

Because of this practical "learning by doing" approach, the **Frontend** codebase might not be perfectly organized or strictly structured yet. However, for the **Backend**, I challenged myself to implement a **Microservices Architecture** to gain hands-on experience with scalable system design. This project is a reflection of my ongoing journey in full-stack development.

---

## ✨ Features

### 🔒 Authentication & Security
* **User Registration & Login:** Full account creation and authentication flow.
* **Email Verification:** Sending verification links via email to activate accounts.
* **Google OAuth:** Seamless login with Google.
* **Session Management (JWT & Cookies):** Generating tokens using `pyjwt`, validating them, and securely storing them via HTTP-only Cookies.
* **Secure Logout:** Safely terminating user sessions.
* **Rate Limiting & Security:** Tracking IP and email login attempts to prevent brute-force attacks and abuse.

### 📚 Content Management (Books & Novels)
* **Data Retrieval:** * Get all books and novels.
  * Filter to get novels only.
  * Filter to get books only.
  * Get specific item by ID.
* **Data Mutation:** Adding and deleting books/novels.
* **User Management:** Admin capabilities to delete users.
* **Pagination:** Efficient data fetching to handle large amounts of content.

### ⚡ Architecture & Performance
* **Backend Architecture:** Built using a **Microservices** approach with FastAPI for modularity and scalability.
* **Caching with Redis:** Frequently fetched pages and queries are cached to significantly reduce server load and improve response times.
* **Multilingual Support:** The platform supports multiple languages using JSON files. User language preferences are stored in Redis for instant retrieval.
* **FastAPI Advanced Features:** Heavy utilization of Middleware and Lifespan events for application state management.
* **Global Error Handling:** Structured and clear error responses across the API.
* **Redis Integration:** Used extensively for caching, storing email verification tokens, tracking IP/email attempts, and saving user preferences.

---

## 🛠️ Tech Stack

**Frontend:**
* HTML5
* CSS3
* Vanilla JavaScript

**Backend:**
* **FastAPI:** High-performance framework used for the microservices.
* **MySQL:** Primary relational database for storing users and content.
* **Redis:** In-memory data store used for caching, rate limiting, and temporary token storage.
