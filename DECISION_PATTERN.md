# Decision Pattern: AI Agent Guardrail

## Purpose
The purpose of this pattern is to demonstrate how an AI agent could classify a request before taking an action.

## Decision Categories

- **ALLOW:** The request has a low risk level.
- **REVIEW:** The request has a medium risk level and needs further review.
- **REJECT:** The request has a high risk level or another unrecognized risk level.

## Example Flow

1. Receive a request.
2. Determine its risk level.
3. Choose an appropriate decision.
4. Allow, review, or reject the request.


