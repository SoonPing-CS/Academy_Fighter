# Example function to generate something
from flask import Flask, render_template, request
from openai import OpenAI
import os, re

client = OpenAI(api_key=os.environ['openai'])


def question(prompt=""):
    system_prompt = """
    You are a mathematic revision question generator. You need to generate the high school question. Only generate the mathematic question in LaTeX format. Do not repeat the generated question. Generate different questions for each time.
    """
    response = client.chat.completions.create(model='gpt-4o',
                                              messages=[{
                                                  'role':
                                                  'system',
                                                  'content':
                                                  system_prompt
                                              }, {
                                                  'role': 'user',
                                                  'content': prompt
                                              }],
                                              temperature=0.9,
                                              max_tokens=1000)

    return response.choices[0].message.content


# Verify the user's answer
def verify_answer3(user_answer, question):
    system_prompt = """
        You are a mathematic solution checker. You need to check the answer and the solution for the question.
        If the answer is correct, return "Correct!".
        If the answer is incorrect, return "Incorrect!". Then show the correct answer and solution in the LaTeX format. Analyz the answer provided and analyz the possible mistake and suggestion.
        """

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'system',
                'content': system_prompt
            },
            {
                'role': 'user',
                'content': 'question: ' + question + '\nanswer: ' + user_answer
            },
        ],
        temperature=0.7,
        max_tokens=1000)
    return response.choices[0].message.content
