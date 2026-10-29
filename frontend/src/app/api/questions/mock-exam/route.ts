import { NextRequest, NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const limit = parseInt(searchParams.get('limit') || '10');
  const unitId = searchParams.get('unit_id');
  const questions = dataStore.getMockExam(limit, unitId);
  return NextResponse.json(questions);
}
