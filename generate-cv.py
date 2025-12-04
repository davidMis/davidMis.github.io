#!/usr/bin/env python3
"""
Generate CV content for Quarto from structured YAML data.
Usage: python generate-cv.py > cv-content.qmd
"""

import yaml

def format_author(author, format_type):
    """Format author names, underlining 'SD Mis'."""
    if author == "SD Mis":
        if format_type == "html":
            return f"[{author}]{{.underline}}"
        else:  # pdf
            return f"\\ul{{{author}}}"
    return author

def format_authors(authors, format_type):
    """Format list of authors."""
    return ", ".join(format_author(a, format_type) for a in authors)

def render_education(data, format_type):
    """Render education section."""
    output = []
    
    for edu in data:
        if format_type == "html":
            output.append(f"**{edu['institution']}**  ")
            
            if 'degree' in edu:
                output.append(f"{edu['degree']}, *{edu['field']}*  ")
            elif 'degrees' in edu:
                for deg in edu['degrees']:
                    output.append(f"{deg['degree']}, *{deg['field']}*  ")
            
            output.append(f"{edu['dates']}, {edu['location']}  ")
            if 'advisor' in edu:
                output.append(f"Advised by {edu['advisor']}")
            output.append("\n")
        else:  # pdf
            content = f"\\cventry{{\\textbf{{{edu['institution']}}}"
            
            if 'degree' in edu:
                content += f" \\\\ {edu['degree']}, \\textit{{{edu['field']}}}"
            elif 'degrees' in edu:
                for deg in edu['degrees']:
                    content += f" \\\\ {deg['degree']}, \\textit{{{deg['field']}}}"
            
            content += f" \\\\ {edu['location']}"
            if 'advisor' in edu:
                content += f" \\\\ Advised by {edu['advisor']}"
            content += f"}}{{{edu['dates']}}}{{}}\n"
            
            output.append(content)
    
    return "\n".join(output)

def render_publications(data, format_type):
    """Render publications section."""
    output = []
    
    # Conference papers
    if 'conference' in data:
        output.append("### Conference papers\n")
        for pub in data['conference']:
            if format_type == "html":
                output.append(f"**{pub['title']}**  ")
                output.append(f"{format_authors(pub['authors'], format_type)}  ")
                output.append(f"*{pub['venue']}*  ")
                output.append(f"{pub['date']}, {pub['location']}  ")
                if 'links' in pub:
                    links = " ".join(f"[[{k}]({v})]" for k, v in pub['links'].items())
                    output.append(links)
                output.append("\n")
            else:  # pdf
                authors_str = format_authors(pub['authors'], format_type)
                content = f"\\cventry{{\\textbf{{{pub['title']}}} \\\\ {authors_str} \\\\ \\textit{{{pub['venue']}}} \\\\ {pub['location']}}}{{{pub['date']}}}{{}}\n"
                output.append(content)
    
    # Journal papers
    if 'journal' in data:
        output.append("\n### Journal papers\n")
        for pub in data['journal']:
            if format_type == "html":
                output.append(f"**{pub['title']}**  ")
                output.append(f"{format_authors(pub['authors'], format_type)}  ")
                venue_text = pub['venue']
                if 'volume' in pub:
                    venue_text += f", {pub['volume']}"
                if 'pages' in pub:
                    venue_text += f", {pub['pages']}"
                output.append(f"*{venue_text}*  ")
                if 'links' in pub:
                    links = " ".join(f"[[{k}]({v})]" for k, v in pub['links'].items())
                    output.append(links)
                output.append("\n")
            else:  # pdf
                authors_str = format_authors(pub['authors'], format_type)
                venue_text = pub['venue']
                if 'volume' in pub:
                    venue_text += f", {pub['volume']}"
                if 'pages' in pub:
                    venue_text += f", {pub['pages']}"
                content = f"\\cventry{{\\textbf{{{pub['title']}}} \\\\ {authors_str} \\\\ \\textit{{{venue_text}}}}}{{{pub['date']}}}{{}}\n"
                output.append(content)
    
    return "\n".join(output)

def render_talks(data, format_type):
    """Render talks section."""
    output = []
    
    for talk in data:
        if format_type == "html":
            output.append(f"**{talk['title']}**  ")
            if 'authors' in talk:
                output.append(f"{format_authors(talk['authors'], format_type)}  ")
            output.append(f"*{talk['venue']}*  ")
            output.append(f"{talk['date']}, {talk['location']}\n")
        else:  # pdf
            content = f"\\cventry{{\\textbf{{{talk['title']}}}"
            if 'authors' in talk:
                authors_str = format_authors(talk['authors'], format_type)
                content += f" \\\\ {authors_str}"
            content += f" \\\\ \\textit{{{talk['venue']}, {talk['location']}}}}}{{{talk['date']}}}{{}}\n"
            output.append(content)
    
    return "\n".join(output)

def render_experience(data, format_type):
    """Render experience section."""
    output = []
    
    for item in data:
        inst = item.get('institution') or item.get('company') or item.get('position', '')
        
        if format_type == "html":
            output.append(f"**{inst}**  ")
            if 'position' in item and (item.get('institution') or item.get('company')):
                output.append(f"*{item['position']}*  ")
            output.append(f"{item['dates']}, {item['location']}  ")
            
            details = item.get('details', '')
            if isinstance(details, list):
                for detail in details:
                    output.append(f"{detail}  ")
            else:
                output.append(f"{details}")
            output.append("\n")
        else:  # pdf
            content = f"\\cventry{{\\textbf{{{inst}}}"
            
            if 'position' in item and (item.get('institution') or item.get('company')):
                content += f" \\\\ \\textit{{{item['position']}}}"
            
            content += f" \\\\ {item['location']} \\\\ "
            
            details = item.get('details', '')
            if isinstance(details, list):
                content += " \\\\ ".join(details)
            else:
                content += details
            
            content += f"}}{{{item['dates']}}}{{}}\n"
            output.append(content)
    
    return "\n".join(output)

def main():
    # Read CV data
    with open('cv-data.yml', 'r') as f:
        cv_data = yaml.safe_load(f)
    
    # Generate both HTML and PDF versions
    for format_type in ['html', 'pdf']:
        print(f"\n::: {{.content-visible when-format=\"{format_type}\"}}")
        print("## Education\n")
        print(render_education(cv_data['education'], format_type))
        print("\n:::\n")
        
        print(f"\n::: {{.content-visible when-format=\"{format_type}\"}}")
        print("## Publications\n")
        print(render_publications(cv_data['publications'], format_type))
        print("\n:::\n")
        
        print(f"\n::: {{.content-visible when-format=\"{format_type}\"}}")
        print("## Talks\n")
        print(render_talks(cv_data['talks'], format_type))
        print("\n:::\n")
        
        print(f"\n::: {{.content-visible when-format=\"{format_type}\"}}")
        print("### Teaching\n")
        print(render_experience(cv_data['experience']['teaching'], format_type))
        print("\n:::\n")
        
        print(f"\n::: {{.content-visible when-format=\"{format_type}\"}}")
        print("### Research\n")
        print(render_experience(cv_data['experience']['research'], format_type))
        print("\n:::\n")
        
        print(f"\n::: {{.content-visible when-format=\"{format_type}\"}}")
        print("### Software Development\n")
        print(render_experience(cv_data['experience']['software'], format_type))
        print("\n:::\n")
        
        print(f"\n::: {{.content-visible when-format=\"{format_type}\"}}")
        print("### Mentorship\n")
        print(render_experience(cv_data['experience']['mentorship'], format_type))
        print("\n:::\n")

if __name__ == "__main__":
    main()
