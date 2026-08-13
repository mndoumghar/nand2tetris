import os
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>CV Mohamed - Développeur Backend & Systèmes</title>
    <style>
        @page {
            size: A4;
            margin: 15mm 12mm;
            background-color: #ffffff;
        }
        
        * {
            box-sizing: border-box;
        }
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #2c3e50;
            font-size: 10.5pt;
            line-height: 1.4;
        }
        
        .header {
            margin-bottom: 20px;
            border-bottom: 2px solid #34495e;
            padding-bottom: 15px;
        }
        
        .header-table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .header-left {
            vertical-align: bottom;
        }
        
        .header-right {
            text-align: right;
            vertical-align: bottom;
            font-size: 9.5pt;
            color: #7f8c8d;
        }
        
        h1 {
            font-size: 24pt;
            color: #2c3e50;
            margin: 0 0 5px 0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .title {
            font-size: 14pt;
            color: #16a085;
            font-weight: bold;
            margin: 0;
        }
        
        h2 {
            font-size: 13pt;
            color: #2c3e50;
            border-left: 4px solid #16a085;
            padding-left: 8px;
            margin: 20px 0 12px 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            page-break-after: avoid;
        }
        
        .section-desc {
            font-style: italic;
            color: #7f8c8d;
            margin-bottom: 10px;
        }
        
        .item {
            margin-bottom: 15px;
            page-break-inside: avoid;
        }
        
        .item-header {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 4px;
        }
        
        .item-title {
            font-weight: bold;
            font-size: 11pt;
            color: #2c3e50;
        }
        
        .item-tech {
            font-weight: bold;
            color: #16a085;
            font-size: 10pt;
        }
        
        .item-date {
            text-align: right;
            color: #7f8c8d;
            font-size: 9.5pt;
        }
        
        .item-subtitle {
            font-style: italic;
            color: #34495e;
            margin-bottom: 5px;
            font-size: 10pt;
        }
        
        ul {
            margin: 0;
            padding-left: 20px;
        }
        
        li {
            margin-bottom: 3px;
        }
        
        .skills-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 5px;
        }
        
        .skills-table td {
            padding: 4px 0;
            vertical-align: top;
        }
        
        .skills-label {
            font-weight: bold;
            width: 25%;
            color: #34495e;
        }
        
        .skills-value {
            width: 75%;
        }
    </style>
</head>
<body>

    <div class="header">
        <table class="header-table">
            <tr>
                <td class="header-left">
                    <h1>Mohamed</h1>
                    <div class="title">Développeur Backend & Systèmes</div>
                </td>
                <td class="header-right">
                    Marrach, Maroc<br>
                    mohamed.developer@email.com<br>
                    +212 600 000000<br>
                    github.com/mohamed-dev
                </td>
            </tr>
        </table>
    </div>

    <h2>Profil Professionnel</h2>
    <p>
        Développeur passionné par la programmation système de bas niveau, les architectures logicielles performantes et la cybersécurité. Fort d'un apprentissage intensif basé sur la réalisation de projets complexes en autonomie et en équipe, je me spécialise dans la conception de solutions robustes et optimisées en utilisant principalement Rust et Go.
    </p>

    <h2>Compétences Techniques</h2>
    <table class="skills-table">
        <tr>
            <td class="skills-label">Langages</td>
            <td class="skills-value">Rust, Go, C, Python, JavaScript</td>
        </tr>
        <tr>
            <td class="skills-label">Systèmes & Outils</td>
            <td class="skills-value">Linux, Architecture des ordinateurs (microarchitectures), Shell UNIX, Git, Docker</td>
        </tr>
        <tr>
            <td class="skills-label">Spécialités</td>
            <td class="skills-value">Programmation système, Algorithmes de routage et graphes, Gestion mémoire, Firmware IoT</td>
        </tr>
    </table>

    <h2>Projets Majeurs</h2>

    <div class="item">
        <table class="item-header">
            <tr>
                <td class="item-title">0-Shell <span class="item-tech">[Rust]</span></td>
                <td class="item-date">2026</td>
            </tr>
        </table>
        <div class="item-subtitle">Développement d'un interpréteur de commandes Unix modulaire</div>
        <ul>
            <li>Implémentation complète de la gestion du cycle de vie des processus et de l'exécution des commandes.</li>
            <li>Conception de mécanismes avancés de redirection des flux d'entrée/sortie et de piping.</li>
            <li>Garantie d'une sécurité mémoire maximale et gestion stricte des erreurs via les paradigmes natifs de Rust.</li>
        </ul>
    </div>

    <div class="item">
        <table class="item-header">
            <tr>
                <td class="item-title">Lem-in <span class="item-tech">[Go]</span></td>
                <td class="item-date">2026</td>
            </tr>
        </table>
        <div class="item-subtitle">Moteur d'optimisation de trajectoire et de gestion de trafic sur graphes</div>
        <ul>
            <li>Développement d'un algorithme de recherche de chemins performant basé sur des variantes de BFS/DFS.</li>
            <li>Résolution de problèmes de flux maximum sous contraintes strictes de ressources et de temps de calcul.</li>
            <li>Optimisation des structures de données pour le traitement efficace de graphes de grande taille.</li>
        </ul>
    </div>

    <div class="item">
        <table class="item-header">
            <tr>
                <td class="item-title">SmartAgri-Rust <span class="item-tech">[Rust / Embedded]</span></td>
                <td class="item-date">2026</td>
            </tr>
        </table>
        <div class="item-subtitle">Prototype IoT d'irrigation de précision</div>
        <ul>
            <li>Écriture de firmware embarqué sur microcontrôleurs ESP32 en utilisant l'écosystème Rust embedded.</li>
            <li>Intégration de capteurs de données environnementales et contrôle déterministe à faible latence.</li>
            <li>Gestion optimisée de la consommation énergétique et de la mémoire vive.</li>
        </ul>
    </div>

    <div class="item">
        <table class="item-header">
            <tr>
                <td class="item-title">Architecture & Microprocesseurs <span class="item-tech">[Hardware Design]</span></td>
                <td class="item-date">2026</td>
            </tr>
        </table>
        <div class="item-subtitle">Implémentation de modules de mémoire vive</div>
        <ul>
            <li>Modélisation et réalisation de puces mémoires fonctionnelles RAM8 et RAM64.</li>
            <li>Analyse approfondie de la logique d'adressage, des multiplexeurs et du comportement microarchitectural.</li>
            <li>Étude pratique des vulnérabilités de bas niveau et des attaques par canal auxiliaire (side-channel).</li>
        </ul>
    </div>

    <h2>Formation & Parcours</h2>

    <div class="item">
        <table class="item-header">
            <tr>
                <td class="item-title">Zone01 Oujda (01Talent)</td>
                <td class="item-date">2026 - Présent</td>
            </tr>
        </table>
        <div class="item-subtitle">Formation d'excellence en informatique - Apprentissage par projets peer-to-peer</div>
        <ul>
            <li>Cursus intensif axé sur le développement logiciel autonome, la résolution de problèmes algorithmiques complexes et l'ingénierie système.</li>
        </ul>
    </div>

    <div class="item">
        <table class="item-header">
            <tr>
                <td class="item-title">Lycée Lalla Khadija</td>
                <td class="item-date">Avant 2026</td>
            </tr>
        </table>
        <div class="item-subtitle">Brevet de Technicien Supérieur (BTS) - Développement des Systèmes d'Information (DSI)</div>
        <ul>
            <li>Formation académique aux bases du développement logiciel, modélisation des données et gestion des architectures de l'information.</li>
        </ul>
    </div>

</body>
</html>
"""

with open("cv_mohamed.html", "w", encoding="utf-8") as f:
    f.write(html_content)

HTML("cv_mohamed.html").write_pdf("cv_mohamed.pdf")
print("PDF successfully generated.")