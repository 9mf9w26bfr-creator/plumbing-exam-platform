import { NextRequest, NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function DELETE(
  _request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const res = dataStore.deleteQuestion(params.id);
    return NextResponse.json(res);
  } catch (err: unknown) {
    return NextResponse.json({ detail: (err as Error).message }, { status: 400 });
  }
}
