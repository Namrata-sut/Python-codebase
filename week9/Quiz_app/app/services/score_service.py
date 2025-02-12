from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from fastapi import Request
from app.models.question_model import Question
from app.models.score_model import Score
from app.models.user_model import User


async def process_quiz_submission(request: Request, db: AsyncSession):
    form_data = await request.form()
    quiz_id_str = form_data.get("quiz_id", "0").strip()
    quiz_id = int(quiz_id_str)
    result = await db.execute(select(Question).where(Question.quiz_id == quiz_id))
    questions = result.scalars().all()
    total_questions = len(questions)

    if total_questions == 0:
        return {"error": "No questions found for this quiz."}

    correct_count = 0

    for question in questions:
        selected_answers = form_data.getlist(f"selected_options_{question.id}[]")
        correct_answers = [question.answer]

        if set(selected_answers) == set(correct_answers):
            correct_count += 1

    score_percentage = (correct_count / total_questions) * 100

    user = User(
        id=1,
        username="Namrata",
        email="Namrata@gmail.com",
        password="Namrata@123",
        role="user"
    )

    score_entry = Score(
        user_id=user.id,
        quiz_id=quiz_id,
        score=score_percentage,
        timestamp=text("'0 seconds'::INTERVAL")
    )

    db.add(score_entry)
    await db.commit()

    return {
        "message": "Quiz submitted successfully!",
        "correct_count": correct_count,
        "total_questions": total_questions,
        "score": score_percentage,
        "quiz_id": quiz_id
    }
