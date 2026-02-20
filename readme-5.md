# Smart Transport Load Balancing System

## Student Details

**Name:** Earla Bhavyanshi

## Personalization Values

* **L (length of name without spaces):** 15
* **PLI = L % 3:** 0

## Applied Rule

Since **PLI = 0**, **Rule A** is applied:

**Rule A:**
All **Overload** package weights are moved to **Invalid Entries**, and the overload list becomes empty after transfer.

---

## Program Description

This Python program helps a logistics company check and organize package weights before transportation.

The program:

* Takes the **number of package weights** from the user
* Accepts each **weight as input**
* Classifies weights into:

  * Very Light
  * Normal Load
  * Heavy Load
  * Overload
  * Invalid Entries
* Counts:

  * **Total valid weights**
  * **Number of affected items** after applying PLI rule
* Displays the **final balanced loading plan**

---

## Constraints Followed

The solution strictly follows the given rules:

* Used **lists, loops, and conditional statements only**
* Did **NOT** use:

  * `append()`
  * list comprehension
  * `sum()`, `max()`, `min()`
  * sorting functions
  * dictionaries or sets

---

## Git Commit History

1. **Initial program to take input and classify package weights**

   * Implemented user input
   * Added weight categorization logic

2. **Added valid weight count and implemented Rule A for overload handling**

   * Calculated total valid weights
   * Applied PLI Rule A to move overload items into invalid entries

3. **Added final output display and completed smart transport load balancing program**

   * Displayed counts, L value, PLI value
   * Printed final categorized loading lists



The program successfully analyzes package weights, applies personalization using **PLI**, and produces a **safe and balanced loading report** for transportation.
