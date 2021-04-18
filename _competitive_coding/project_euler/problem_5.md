---
layout: archive
title: "Problem 5"
permalink: /competitive_coding/project_euler/problem_5/
author_profile: true
redirect_from:
    - /competitive_coding/project_euler/problem_5
    - /competitive_coding/project_euler/problem_5.md
---
<link rel="stylesheet" href="/_competitive_coding/project_euler/project_euler_problem.css" type="text/css">

{% include base_path %}

<h3><a href="/competitive_coding/project_euler_home/">Return to Problem List</a></h3>

<h2 class="_5p">Smallest multiple: 5%</h2>
<div class="problem_content">
<p>2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.</p>
<p>What is the smallest positive number that is <dfn title="divisible with no remainder">evenly divisible</dfn> by all of the numbers from 1 to 20?</p>
</div>

## My Solution

I solved this problem on June 9, 2018. As of April 17, 2021, this problem has been solved by 492,154 other members. 

This problem is so simple it does not require any code at all. Simply break down the integers from 2 - 20 into their constituent factors and choose only the factors which are necessary to create each integer less than 20. Multiply them together to get the answer.

### Python 3

<script src="https://gist.github.com/NolantheNerd/2944243db34f9ac7b6fc851856f94a2c.js"></script>