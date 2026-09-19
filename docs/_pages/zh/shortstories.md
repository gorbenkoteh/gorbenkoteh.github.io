---
layout: page
title: 故事
permalink: /zh/shortstories/
description: 短篇故事
nav: true
nav_order: 9
lang: zh
lang_ref: /shortstories/
display_categories: [shortstories_zh]
horizontal: false
---

<!-- _pages/zh/shortstories.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  {% for category in page.display_categories %}
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <div class="grid">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endfor %}
{% endif %}
</div>
