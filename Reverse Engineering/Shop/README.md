# Shop - Reverse Engineering Challenge

## Challenge Overview
**Name:** Shop  
**Category:** Reverse Engineering  
**Points:** 50

## Objective

The objective of the "Shop" challenge is to obtain the flag by exploiting a logic flaw in the program without the need for reversing the binary. The primary exploit involves buying negative items, which results in a gain of coins.

## Solution Steps

To solve this challenge, follow these steps:

1. **Analyze the Binary:**
   - Begin by running the provided binary.
   - Observe that this is a simple shop program that allows you to buy items and accumulate coins.

2. **Exploit Negative Item Purchase:**
   - To exploit the program, buy negative quantities of items. This is where the vulnerability lies.
   - The calculation for coins typically involves the formula: `ur_coins = ur_coins - (item_price * amount_buying)`.

3. **Gain Coins:**
   - When you buy negative items (i.e., by specifying a negative quantity), you are essentially adding coins to your account. This occurs because the product of "item_price" and "amount_buying" is negative.

4. **Buy the Flag:**
   - Once you have a sufficient amount of coins, proceed to buy the flag from the shop.
   - The flag is available for purchase for 100 coins.

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
