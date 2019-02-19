from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField, FileField
from wtforms.validators import Required

class AddBlog(FlaskForm):
    title = StringField("Blog Title", validators = [Required()])
    blog = TextAreaField("Description", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("interview", "interview"),("funny","funny"),("promotion","promotion"),("product","product"),("random","random")],validators = [Required()]
    )
    submit = SubmitField("Add blog")

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')