import { NextRequest, NextResponse } from 'next/server';
import { dataStore } from '@/data/store';
import { QuestionStatus } from '@/types';

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const status = (searchParams.get('status') as QuestionStatus) || undefined;
  const keyword = searchParams.get('keyword') || undefined;
  const chapter_id = searchParams.get('chapter_id') ? parseInt(searchParams.get('chapter_id')!) : undefined;
  const unit_id = searchParams.get('unit_id') || undefined;

  const questions = dataStore.getCMSQuestions({ status, keyword, chapter_id, unit_id });
  return NextResponse.json(questions);
}

export async function POST(request: NextRequest) {
  try {
    const payload = await request.json();
    const created = dataStore.createQuestion(payload);
    return NextResponse.json(created, { status: 201 });
  } catch (err: unknown) {
    return NextResponse.json({ detail: (err as Error).message }, { status: 400 });
  }
}
