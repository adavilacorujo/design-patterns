# Factory design pattern

This is my attempt at simulating a program that follows a factory design pattern.

# Intro

The application mimics fetching events from email service providers, ie Gmail, Yahoo, Protonmail. The implementation is very rudimentary. In this implementation, we could add more providers by creating their implementations and then adding them to the Events class.

## Structure

Everything related to fetching the data from the providers is under _events_.
Everything related to mimicing a server is under _server_.

![alt text](./images/factory.jpg)
