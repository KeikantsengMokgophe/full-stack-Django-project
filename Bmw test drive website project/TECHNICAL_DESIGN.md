## Technical Design

The BMW Test Drive Booking App follows Django's
Model–View–Template (MVT) architecture.

### Architecture
- Models manage vehicle, user and booking data.
- Views handle requests, business logic and validation.
- Templates render the user interface.
- URL configurations connect requests to views.
- SQLite stores application data during development.

### User Roles
- Customer: registers, logs in, browses vehicles,
  requests test drives and views their bookings.
- Administrator: manages vehicle listings and
  oversees bookings.

### Technology Stack
- Python and Django
- HTML and CSS
- Django Template Language
- SQLite
- Git and GitHub

For the full design, see [TECHNICAL_DESIGN.md](TECHNICAL_DESIGN.md).
