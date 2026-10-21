# CIIFA team profile generator

Workflow:
1. Share `CIIFA-Team-Profile-Form.html` with each team member (WhatsApp/email attachment).
   They open it in any browser (phone or laptop, no internet needed), fill it,
   add a headshot, and a single `ciifa-profile-<name>.json` downloads (photo embedded).
2. Collect those files into `profiles/` here.
3. Run:  python build_team.py
4. You get, per person:
   - `out/<name>-card.png`         branded 1080x1350 profile card (social/press)
   - `../site/assets/img/team/<name>.jpg`  headshot for the website
   - `out/team-cards.html`         cards to paste into site/team.html (replaces the
                                   initials cards; CSS class .avatar-img already live)
5. Deploy the site as usual.

`profiles/` and `out/` are gitignored: personal data and photos never enter the public repo.
