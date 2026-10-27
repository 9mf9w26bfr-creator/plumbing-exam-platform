import { NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function GET() {
  const stats = dataStore.getCMSStats();
  return NextResponse.json(stats);
}
