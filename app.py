from flask import Flask, render_template, request
from openai import OpenAI
app = Flask(__name__)
client = OpenAI()