from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL
#from flask_ckeditor import CKEditorField


##WTForm
class CreateEventForm(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    subtitle = StringField("Academic Year", validators=[DataRequired()])
    group = StringField("Group Members", validators=[DataRequired()])
    guide = StringField("Project Guide", validators=[DataRequired()])
    img_url = StringField("Project Image URL", validators=[DataRequired(), URL()])
    body = StringField("Project Content", validators=[DataRequired()])
    submit = SubmitField("Create")

class RegisterForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    comment = StringField("Your views about this project", validators=[DataRequired()])
    submit = SubmitField("Comment")

class GrievanceForm(FlaskForm):
    choices = ["Project", "Other"]
    user_choice = SelectField("Type of issue", choices=choices, validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    phone_no = StringField("Phone number")
    grievance = StringField("Tell us about your issue", validators=[DataRequired()])
    submit = SubmitField("Send")

# class LostFoundForm(FlaskForm):
#     choices = ["Lost", "Found"]
#     user_choice = SelectField("Choose one", choices=choices, validators=[DataRequired()])
#     title = StringField("Title", validators=[DataRequired()])
#     item_desc = CKEditorField(f"Tell something about the item , enter your desired way of contact", validators=[DataRequired()])
#     submit = SubmitField("Post")





# class CanteenForm(FlaskForm):
#     name = StringField("Your name", validators=[DataRequired()])
#     order = CKEditorField("Enter your order in the form 'quantity' x 'menu item name' ", validators=[DataRequired()])
#     submit = SubmitField("Order")
