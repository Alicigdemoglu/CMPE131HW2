from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class TopCities(FlaskForm):
    city_name = StringField('city name', validators=[DataRequired(), Length(min=3, max=30)])
    city_rank = IntegerField('city rank', validators=[DataRequired()])
    is_visited = BooleanField('visited')

    submit = SubmitField('submit')
