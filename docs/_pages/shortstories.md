---
layout: page
permalink: /shortstories/
title: Рассказы
description: Рассказы
nav: true
nav_order: 9
lang: ru
lang_ref: /en/shortstories/
display_categories: [shortstories]
horizontal: false
---

<!-- pages/shortstories.md -->
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
