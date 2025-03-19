# pipeline_fun
_Personal Project - Data Pipeline Sandbox_

<div style="display: flex; align-items: flex-start;">

  <div style="margin-right: 16px;">
    <img src="Pipeline_Documentation/images/rainbow_gummi_illustration.png" alt="Pokemon Mystery Dungeon Rainbow Gummi" width="250">
  </div>

  <div>
    <blockquote>Anyone else remember the attribute <code>Funnel Fun</code> from <a href="https://mysterydungeon.pokemon.com/en-us/">Pokemon Mystery Dungeon</a>? No? Just me?</blockquote>
    <small><em><a href="https://bulbapedia.bulbagarden.net/wiki/Gummi#/media/File:Rainbow_Gummi_artwork_RTDX.png">(Image Source)</a></em></small>
  </div>
</div>

<table>
  <tr>
    <td>
      <img src="Pipeline_Documentation/images/rainbow_gummi_illustration.png" alt="Pokemon Mystery Dungeon Rainbow Gummi" width="250">
    </td>
    <td>
      <blockquote>Anyone else remember the attribute <code>Funnel Fun</code> from <a href="https://mysterydungeon.pokemon.com/en-us/">Pokemon Mystery Dungeon</a>? No? Just me?</blockquote>
      <small><em><a href="https://bulbapedia.bulbagarden.net/wiki/Gummi#/media/File:Rainbow_Gummi_artwork_RTDX.png">(Image Source)</a></em></small>
    </td>
  </tr>
</table>

## Introduction
This is a personal sandbox for playing around with different data pipelines, Airflow orchestration, and data validation leveraging Airflow and Python libraries primarily.

In this project, I will also attempt to build a good documentation strategy for pipeline management, since I believe that is directly correlated with data engineering success on projects.

## Pipeline Table of Contents
[Find more about each individual pipeline here](Pipeline_Documentation)

#### Personal Library (Book) CSV Reader
Reads a defined CSV containing columns relevant to books in a personal library, validates some formatting, corrects formatting issues, and returns a corrected CSV.
