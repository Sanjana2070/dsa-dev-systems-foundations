# Interview Questions and Answers

## React

**1. What is the difference between controlled and uncontrolled components in React?**

Controlled components rely on React state to manage form inputs, while uncontrolled components use the DOM directly via refs.

**2. Explain how the `useEffect` hook works.**

`useEffect` runs after the component mounts or updates. It can take a dependency array to control when it runs.

**3. What is prop drilling and how can it be avoided?**

Prop drilling is passing props through many levels of components. It can be avoided using Context API or state management libraries like Redux.

**4. What is React.memo and when should you use it?**

`React.memo` prevents unnecessary re-renders by memoizing functional components based on props.

**5. How does React handle the virtual DOM?**

React creates a virtual copy of the DOM and compares it with the real DOM (diffing), then efficiently updates only the changed parts.

## JavaScript

**1. Explain hoisting in JavaScript.**

Hoisting moves declarations to the top of their scope. `var` is hoisted and initialized as `undefined`, while `let` and `const` are hoisted but not initialized.

**2. What are closures in JavaScript?**

A closure is a function that retains access to its lexical scope even after the outer function has returned.

**3. What is the event loop in JavaScript?**

The event loop handles async operations by placing them in the callback queue and executing them after the main thread is free.

**4. Difference between `==` and `===`?**

`==` checks for value equality with type coercion. `===` checks for strict equality without coercion.

**5. What are Promises and async/await?**

Promises represent future values; async/await is syntactic sugar for handling promises in a more readable way.

## Databases

**1. SQL vs NoSQL - when to use which?**

SQL is structured and relational, great for transactions. NoSQL is schema-less, suitable for flexible, scalable, or nested data.

**2. What is normalization in databases?**

Normalization is the process of reducing redundancy by organizing fields and tables in a relational database.

**3. What are indexes in MongoDB?**

Indexes improve query performance by allowing the database to find data without scanning every document.

**4. How do transactions work in databases?**

Transactions ensure ACID properties: Atomicity, Consistency, Isolation, Durability. In MongoDB, transactions are supported in replica sets.

**5. How would you design a schema for a booking system?**

Use collections for Users, Classes, Bookings; use references for relations and indexes for fast access.

## Backend

**1. What is the role of Express in a Node.js application?**

Express is a minimal and flexible Node.js framework for building web applications and APIs.

**2. What are RESTful APIs?**

RESTful APIs follow standard HTTP methods (GET, POST, PUT, DELETE) and use stateless operations for communication between client and server.

**3. How do you handle authentication in a backend?**

Common methods include sessions, JWT tokens, and OAuth providers like Google (via Supabase, Passport, etc.).

**4. What is CORS and how do you enable it?**

CORS is a security feature that restricts resource access between origins. In Express, enable it via the `cors` middleware.

**5. How do you connect Express to MongoDB?**

Use the `mongoose` library to connect via a URI, define schemas, and perform CRUD operations on MongoDB documents.

