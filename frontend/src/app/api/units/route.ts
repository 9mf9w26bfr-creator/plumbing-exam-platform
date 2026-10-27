import { NextResponse } from 'next/server';
import { dataStore } from '@/data/store';

export async function GET() {
  const units = dataStore.getUnits();
  return NextResponse.json(units);
}
