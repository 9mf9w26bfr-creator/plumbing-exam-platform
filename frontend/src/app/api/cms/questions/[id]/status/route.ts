import { NextRequest, NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function POST(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const { status } = await request.json();
    const updated = dataStore.updateQuestionStatus(params.id, status);
    return NextResponse.json(updated);
  } catch (err: unknown) {
    return NextResponse.json({ detail: (err as Error).message }, { status: 400 });
  }
}
