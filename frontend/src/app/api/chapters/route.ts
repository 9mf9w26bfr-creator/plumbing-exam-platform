import { NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function GET() {
  const chapters = dataStore.getChapters();
  return NextResponse.json(chapters);
}
