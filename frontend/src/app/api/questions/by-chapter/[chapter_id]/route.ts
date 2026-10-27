import { NextRequest, NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function GET(
  request: NextRequest,
  { params }: { params: { chapter_id: string } }
) {
  const chapterId = parseInt(params.chapter_id);
  const { searchParams } = new URL(request.url);
  const subTopicId = searchParams.get('sub_topic_id');

  const questions = dataStore.getQuestionsByChapter(chapterId, subTopicId);
  return NextResponse.json(questions);
}
