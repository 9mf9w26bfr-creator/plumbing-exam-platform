import { NextRequest, NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function GET(
  _request: NextRequest,
  { params }: { params: { unit_id: string } }
) {
  const unitId = params.unit_id;
  const questions = dataStore.getQuestionsByUnit(unitId);
  return NextResponse.json(questions);
}
