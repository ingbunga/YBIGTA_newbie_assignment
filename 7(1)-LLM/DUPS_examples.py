DUPS_EXAMPLE_TEXT = """[Example 1]
Question: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Here are the results:

Core Question: How many clips did Natalia sell altogether in April and May?

Hints:

1. Natalia sold clips to 48 friends in April.
2. She sold half as many clips in May as she did in April.

Reason Steps:

1. Let's first find out how many clips Natalia sold in May. Since she sold half as many clips in May as she did in April, and she sold 48 clips in April, she sold 48/2 = 24 clips in May.
2. To find the total number of clips Natalia sold, we add the number of clips she sold in April and May: 48 + 24 = 72.

#### 72


[Example 2]
Question: Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?
Here's the solution:

Core Question: How much more money does Betty need to buy the wallet?

Hints:

1. Betty needs $100 for the wallet.
2. She has half of the money she needs.
3. Her parents gave her $15.
4. Her grandparents gave her twice as much as her parents.

Reason Steps:

1. Since Betty has half of the money she needs, she needs $100 - ($100/2) = $50 more.
2. Her parents gave her $15, so she has $15 more.
3. Her grandparents gave her twice as much as her parents, so they gave her 2 x $15 = $30.
4. In total, Betty has $15 + $30 = $45.
5. She still needs $50 - $45 = $5 more.

#### $5


[Example 3]
Question: Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?
Here are the extracted information and the answer:

Core Question: How many pages should Julie read tomorrow to read half of the remaining pages?

Hints:

1. Julie is reading a 120-page book.
2. She read 12 pages yesterday.
3. She read twice as many pages as yesterday today.
4. She wants to read half of the remaining pages tomorrow.

Reason Steps:

1. Let's calculate the total number of pages Julie has read so far: 12 (yesterday) + 2 * 12 (today) = 36 pages.
2. The remaining pages are: 120 - 36 = 84 pages.
3. Julie wants to read half of the remaining pages tomorrow, which is: 84 / 2 = 42 pages.

#### 42


[Example 4]
Question: James writes a 3-page letter to 2 different friends twice a week.  How many pages does he write a year?
Here are the results:

Core Question: How many pages does James write in a year?

Hints:

* James writes a 3-page letter to 2 different friends
* He writes twice a week
* He writes a year

Reason Steps:

1. James writes 3-page letters to 2 different friends, so he writes a total of 3 x 2 = 6 pages per letter-writing session.
2. He writes twice a week, so he writes 6 pages x 2 = 12 pages per week.
3. There are 52 weeks in a year, so James writes 12 pages x 52 weeks = 624 pages in a year.

#### 624


[Example 5]
Question: Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?
Here are the requested outputs:

Core Question: How many flowers does Mark have in his garden?

Hints:

1. There are 10 yellow flowers.
2. There are 80% more purple flowers than yellow flowers.
3. There are 25% as many green flowers as there are yellow and purple flowers.

Reason Steps:

1. Let's find the number of purple flowers. Since there are 80% more purple flowers than yellow flowers, we can set up the equation: Purple flowers = 10 + (80% of 10) = 10 + 8 = 18.
2. The total number of yellow and purple flowers is 10 (yellow) + 18 (purple) = 28.
3. Since there are 25% as many green flowers as there are yellow and purple flowers, we can set up the equation: Green flowers = 25% of 28 = 0.25 x 28 = 7.
4. The total number of flowers is the sum of yellow, purple, and green flowers: 10 (yellow) + 18 (purple) + 7 (green) = 35.

#### 35


[Example 6]
Question: Albert is wondering how much pizza he can eat in one day. He buys 2 large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8 slices. If he eats it all, how many pieces does he eat that day?
Here's the solution:

Core Question: How many pieces of pizza does Albert eat in one day?

Hints:

1. Albert buys 2 large pizzas and 2 small pizzas.
2. A large pizza has 16 slices.
3. A small pizza has 8 slices.

Reason Steps:

1. First, we need to find the total number of slices from the large pizzas. Since Albert buys 2 large pizzas, we multiply the number of slices per pizza (16) by 2: 16 x 2 = 32 slices.
2. Next, we need to find the total number of slices from the small pizzas. Since Albert buys 2 small pizzas, we multiply the number of slices per pizza (8) by 2: 8 x 2 = 16 slices.
3. Finally, we add the total number of slices from the large pizzas and small pizzas to find the total number of slices Albert can eat: 32 + 16 = 48 slices.

#### 48


[Example 7]
Question: Ken created a care package to send to his brother, who was away at boarding school.  Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds.  Then, he added enough brownies to cause the weight to triple.  Next, he added another 2 pounds of jelly beans.  And finally, he added enough gummy worms to double the weight once again.  What was the final weight of the box of goodies, in pounds?
Here are the results:

Core Question: What was the final weight of the box of goodies, in pounds?

Hints:

1. The box started with a weight of 0 pounds.
2. The weight of the box increased by 2 pounds when Ken added jelly beans.
3. The weight of the box tripled when Ken added brownies.
4. The weight of the box increased by 2 pounds again when Ken added more jelly beans.
5. The weight of the box doubled again when Ken added gummy worms.

Reason Steps:

1. The box started with a weight of 0 pounds.
2. Ken added enough jelly beans to bring the weight to 2 pounds, so the weight is now 2 pounds.
3. Ken added enough brownies to triple the weight, so the weight is now 2 x 3 = 6 pounds.
4. Ken added another 2 pounds of jelly beans, so the weight is now 6 + 2 = 8 pounds.
5. Ken added enough gummy worms to double the weight again, so the weight is now 8 x 2 = 16 pounds.

#### 16


[Example 8]
Question: Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?
Here is the solution:

Core Question: How much did Alexis pay for the shoes?

Hints:

1. Alexis spent a total of $30 + $46 + $38 + $11 + $18 = $143 on the other items.
2. She has $16 left from her budget, which means she spent $200 - $16 = $184 in total.
3. The total amount spent on other items is $143, so the amount spent on shoes is the difference between the total amount spent and the amount spent on other items, which is $184 - $143 = ?

Reason Steps:

1. Calculate the total amount spent on other items: $30 + $46 + $38 + $11 + $18 = $143
2. Calculate the total amount spent: $200 - $16 = $184
3. Calculate the amount spent on shoes: $184 - $143 = $41

#### $41


[Example 9]
Question: Tina makes $18.00 an hour.  If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage.  If she works 10 hours every day for 5 days, how much money does she make?
Here's the solution:

Core Question: How much money does Tina make if she works 10 hours every day for 5 days?

Hints:

1. Tina's hourly wage is $18.00.
2. She is eligible for overtime if she works more than 8 hours per shift.
3. Overtime is paid at a rate of 1.5 times her hourly wage.

Reason Steps:

1. Calculate Tina's total hours worked in 5 days: 10 hours/day × 5 days = 50 hours
2. Calculate Tina's regular hours worked: 8 hours/day × 5 days = 40 hours
3. Calculate Tina's overtime hours worked: 50 hours - 40 hours = 10 hours
4. Calculate Tina's regular pay: 40 hours × $18.00/hour = $720.00
5. Calculate Tina's overtime pay: 10 hours × ($18.00/hour + $9.00/hour) = 10 hours × $27.00/hour = $270.00
6. Calculate Tina's total pay: $720.00 + $270.00 = $990.00

#### $990.00"""

DUPS_EXAMPLES = DUPS_EXAMPLE_TEXT.split('\n\n\n')