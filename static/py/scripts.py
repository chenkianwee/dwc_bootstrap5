from pyscript import document, window
# just something
def highlight_nav(event=None):
    # 1. Get the current URL path
    current_href = window.location.href
    
    # 2. Select all navbar links
    nav_links = document.querySelectorAll('.navbar-nav .nav-link')
    
    for link in nav_links:
        # Prepare segments for folder comparison
        segments = [s for s in current_href.split('/') if s]
        folder_name = segments[-2].lower() if len(segments) >= 2 else ""
        # 3. Get attributes from the link
        link_href = link.href
        dropdown_segs = [s for s in link_href.split('/') if s]
        dropdown_name = dropdown_segs[-1].lower()
        # 4. Logical check for active state
        if current_href == link_href:
            link.classList.add('active')
            link.setAttribute('aria-current', 'page')
        else:
            if len(segments) >= 4 and folder_name == dropdown_name:
                link.classList.add('active')
                link.setAttribute('aria-current', 'page')
            else:
                link.classList.remove('active')

def highlight_vnav(event=None):
    # Get the current URL path
    current_href = window.location.href
    # Select all navbar links
    nav_links = document.querySelectorAll('.list-group .list-group-item')
    for link in nav_links:
        # Get attributes from the link
        link_href = link.href
        # Logical check for active state
        if current_href == link_href:
            link.classList.add('active')
            link.setAttribute('aria-current', 'page')
        else:
            link.classList.remove('active')

# Execute on load
highlight_nav()
highlight_vnav()