---
layout: page
title: Short stories
permalink: /en/shortstories/
description: Short stories
nav: true
nav_order: 9
lang: en
lang_ref: /shortstories/
display_categories: [shortstories_en]
horizontal: false
---

<!-- _pages/en/shortstories.md -->
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
