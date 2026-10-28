import { TextbookChapter, ExamUnit, Question } from '../types';
import questionsBank from './questions_bank.json';

export const initialChapters: TextbookChapter[] = [
  {
    id: 1,
    title: 'Health and safety practices and systems',
    sub_topics: [
      { id: '1.1', title_en: 'Health and safety legislation & regulations', title_zh: '健康與安全法規與條例' },
      { id: '1.2', title_en: 'Personal protective equipment (PPE)', title_zh: '個人防護裝備 (PPE)' },
      { id: '1.3', title_en: 'Safe working at height & ladders', title_zh: '高空作業安全與梯子規範' },
      { id: '1.4', title_en: 'Hazard identification and risk assessment', title_zh: '危險源識別與風險評估' }
    ],
    question_count: 50
  },
  {
    id: 2,
    title: 'Common processes and techniques',
    sub_topics: [
      { id: '2.1', title_en: 'Hand and power tools safety and maintenance', title_zh: '手動與電動工具安全及維護' },
      { id: '2.2', title_en: 'Pipe jointing techniques (soldering, compression)', title_zh: '管道連接技術 (焊接、卡壓)' },
      { id: '2.3', title_en: 'Pipe bending and clipping', title_zh: '管道彎曲與管卡固定' }
    ],
    question_count: 50
  },
  {
    id: 3,
    title: 'Scientific principles',
    sub_topics: [
      { id: '3.1', title_en: 'Units of measurement (SI Units)', title_zh: '國際單位制與測量單位' },
      { id: '3.2', title_en: 'Properties of water & state changes', title_zh: '水的物理性質與狀態改變' },
      { id: '3.3', title_en: 'Pressure and head calculation', title_zh: '水壓與水頭計算' },
      { id: '3.4', title_en: 'Heat transfer (conduction, convection, radiation)', title_zh: '熱傳遞原理 (傳導、對流、輻射)' }
    ],
    question_count: 50
  },
  {
    id: 4,
    title: 'Planning and supervision',
    sub_topics: [
      { id: '4.1', title_en: 'Material estimating and ordering', title_zh: '材料預估與採購' },
      { id: '4.2', title_en: 'Liaison with other building trades', title_zh: '與其他建築工種的協同溝通' }
    ],
    question_count: 50
  },
  {
    id: 5,
    title: 'Cold water systems',
    sub_topics: [
      { id: '5.1', title_en: 'Direct and indirect cold water supply', title_zh: '直接式與間接式冷水供水系統' },
      { id: '5.2', title_en: 'Cold water storage cisterns (CWSC)', title_zh: '冷水儲水箱規格與安裝' },
      { id: '5.3', title_en: 'Water regulations and backflow prevention', title_zh: '水事法規與防回流污染等級 (Fluid Categories)' }
    ],
    question_count: 50
  },
  {
    id: 6,
    title: 'Hot water systems',
    sub_topics: [
      { id: '6.1', title_en: 'Vented hot water storage systems', title_zh: '開式(通風型)熱水儲水系統' },
      { id: '6.2', title_en: 'Unvented hot water storage & safety controls', title_zh: '閉式(承壓型)熱水儲水系統與三級安全保護' },
      { id: '6.3', title_en: 'Legionella prevention and TMV regulation', title_zh: '軍團菌防治與恆溫混水閥 (TMV) 控制' }
    ],
    question_count: 50
  },
  {
    id: 7,
    title: 'Central heating systems',
    sub_topics: [
      { id: '7.1', title_en: 'Heat emitters and pipe sizing', title_zh: '散熱器類型與管徑計算' },
      { id: '7.2', title_en: 'System controls (S-Plan, Y-Plan, TRVs)', title_zh: '供暖控制系統 (S-Plan, Y-Plan, 恆溫閥)' }
    ],
    question_count: 50
  },
  {
    id: 8,
    title: 'Rainwater systems',
    sub_topics: [
      { id: '8.1', title_en: 'Gutters and downpipes sizing', title_zh: '天溝與落水管尺寸規劃' },
      { id: '8.2', title_en: 'Rainwater harvesting principles', title_zh: '雨水收集利用基本原理' }
    ],
    question_count: 50
  },
  {
    id: 9,
    title: 'Sanitation systems',
    sub_topics: [
      { id: '9.1', title_en: 'Sanitary appliances installation', title_zh: '衛生器具安裝要求與間距' },
      { id: '9.2', title_en: 'Discharge stack systems and trap seal loss', title_zh: '排水立管系統與存水彎水封防破壞' }
    ],
    question_count: 50
  },
  {
    id: 10,
    title: 'Domestic fuel systems',
    sub_topics: [
      { id: '10.1', title_en: 'Fuel storage and supply guidelines', title_zh: '燃料儲存與輸送指引' },
      { id: '10.2', title_en: 'Combustion and ventilation requirements', title_zh: '燃燒與通風要求' }
    ],
    question_count: 50
  },
  {
    id: 11,
    title: 'Electrical principles and processes for building services engineering',
    sub_topics: [
      { id: '11.1', title_en: 'Basic electrical safety and safe isolation', title_zh: '電氣安全基礎與安全隔離五步法' },
      { id: '11.2', title_en: 'Bathroom zoning (Zone 0, 1, 2) and IP ratings', title_zh: '浴室電氣分區 (Zone 0, 1, 2) 與 IP 防護等級' },
      { id: '11.3', title_en: 'Equipotential bonding and earthing', title_zh: '等電位聯結與接地保護' }
    ],
    question_count: 50
  }
];

export const initialUnits: ExamUnit[] = [
  { id: 'Unit_201', title: 'Health & Safety', category: 'Core', question_count: 50 },
  { id: 'Unit_202', title: 'Scientific Principles', category: 'Core', question_count: 50 },
  { id: 'Unit_203', title: 'Common Plumbing Processes', category: 'Core', question_count: 50 },
  { id: 'Unit_204', title: 'Cold Water Systems', category: 'Technical', question_count: 50 },
  { id: 'Unit_205', title: 'Hot Water Systems', category: 'Technical', question_count: 50 },
  { id: 'Unit_206', title: 'Sanitation & Drainage', category: 'Technical', question_count: 100 },
  { id: 'Unit_207', title: 'Central Heating Systems', category: 'Technical', question_count: 100 },
  { id: 'Unit_208', title: 'Electrical Principles', category: 'Technical', question_count: 50 },
  { id: 'Unit_209', title: 'Communication / Planning', category: 'Professional', question_count: 50 },
  { id: 'Unit_ENV', title: 'Environmental Revision', category: 'Environmental Revision', question_count: 50 }
];

export const initialQuestions: Question[] = questionsBank as Question[];
