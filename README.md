# PatchWords
A collaborative story telling platform made with Django. For Web App Development 2, team Rango Unchained.


# Database & Form Layouts
## Database
**User**
- profile_picture
- bio
- age
- gender

**Story**
- date/time
- title
- author
- category
- slug

**Paragraph**
- date/time
- story
- parent
- content
- author
- end

**Category**
- name

**Like**
- user
- paragraph

**Favourite**
- user
- story

##Forms

**NewStory**
- Title
- Content
- Category

**NewParagraph**
- content
- parent

**Search**
- keywords

**Like**
- paragraph
- type (either like or dislike (like being true/ticked and unlike being false/untick))

**Favourite**
- Story
- type (either favourite or unfavourite (favourite being true/ticked and unfavourite being false/untick))


# To Do List

###Database
- User
- Story
- Category
- Paragraph
- Like
- Favourite

###Forms
- NewStory
- NewParagraph
- Search
- Like
- Favourite

### Views
- home
- user
- category
- story
- search
- settings
- about

###### Views for forms/javascript

- new_story
- new_paragraph
- favourite
- like
- load_stories
- load_subtree

### Templates
- base
- home
- user
- category
- story
- search
- settings
- about

###### Templates for Auth Redux

- login
- register

###### Templates for parts of the page fetched with javascript

- tree (Used to render a chunk of the tree as HTML to send to the client.)
- stories (Used to render a list of stories to send to the client.)


### Javascript

- Detect scroll and fetch stories.
- Detect paragraph click and carousel left/right.
- Load subtree in to webpage.
- ? Possibly detect favourite/like clicks and toggle icon colour ?
