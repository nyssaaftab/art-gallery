PRD — Community Art Reflection Widget (Updated)
1. Purpose
Create a lightweight, daily art experience that surfaces artworks from major museum APIs and pairs them with short, anonymous reflections left by other users.
 Core goal: the widget drives habit-forming daily engagement.
 Secondary goal: the PWA funnels users to install the widget while providing a shared initial artwork experience.

2. Product Overview
Widget: randomized artwork per user, refreshed daily by default, with optional custom refresh frequency.


PWA:


First load shows a global daily artwork (everyone sees the same piece).


Additional interactions (refresh / “next”) generate randomized artwork per user, mimicking the widget experience.


Users can view a note from a prior user and leave their own reflection.


Anonymous usage; low barrier to entry.



3. Target Users
Casual art lovers seeking daily, low-friction engagement.


Users who enjoy reflection or journaling with art.


Users interested in brief, intimate art experiences on mobile devices.



4. Goals & Success Metrics
Primary Goals
Habit formation via daily widget interaction.


Community-driven reflections.


Easy access / minimal friction to start (anonymous, no signup).


Success Metrics
DAU for widget and PWA.


Notes submitted per artwork.


Widget retention rate.


PWA-to-widget conversion rate.



5. Core Features
5.1 Widget
Shows a random artwork per user daily.


Optionally, users can change refresh frequency: daily, twice a day, weekly.


Tapping opens minimal companion app view for submitting or reading notes.


Pulls content from Python backend API.


5.2 PWA
First load: global daily artwork, consistent for all users.


Subsequent refreshes: randomized artwork per user.


Users see one note per artwork or prompt to leave the first note.


Encourages installation of the widget for daily habit.


5.3 Anonymous Notes
Users identified via a UUID stored locally.


No authentication needed for MVP.


Notes stored with artwork_id, user_id, text, timestamp.



6. Non-Goals
Social feed, likes, or follow system.


Complex moderation (beyond basic profanity filter).


Multi-artwork browsing or feeds.


Account signup / login for MVP.



7. Technical Overview
7.1 Backend
Python + FastAPI


Responsibilities:


Fetch & cache artworks from Chicago Art Institue API
Weighted random selection for notes/artworks


Store & retrieve anonymous reflections


Track last fetch per user for randomized widget refresh frequency


7.2 Database
MongoDB Atlas or PostgreSQL


Tables / Collections:


artworks → id, title, artist, image_url, museum_source


notes → id, artwork_id, user_id, text, timestamp


users → id (UUID), refresh_interval, last_widget_fetch_timestamp


7.3 Frontend / PWA
React + Vercel


Initial load: global artwork


Refresh: randomized per user


Stores anonymous UUID in localStorage


7.4 Backend Hosting
Persistent Python backend on Render or Railway


Serves both widget and PWA API requests



8. API Requirements
GET /artwork/today?mode=global
Returns today’s global artwork for all users.


GET /artwork/today?mode=random&user_id=UUID
Returns randomized artwork for a user, respecting widget refresh frequency.


GET /artwork/{id}/note
Returns a random reflection for the artwork.


POST /artwork/{id}/note
Body: { user_id, text }


Stores anonymous reflection.



9. UX Principles
Quiet, minimal UI; artwork is the focus.


Personal discovery in widget; shared ritual for first-time PWA users.


Anonymous participation to reduce friction and anxiety.



10. Future Enhancements
Widget refresh frequency settings.


Weekly “popular artworks” leaderboard.


Push notifications for PWA & widget.


Expanded museum sources, themes, and user-curated collections.

