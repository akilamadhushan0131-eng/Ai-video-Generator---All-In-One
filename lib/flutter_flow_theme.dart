import 'package:flutter/material.dart';

class FlutterFlowTheme {
  static FlutterFlowTheme of(BuildContext context) => FlutterFlowTheme();

  TextStyle get bodyMedium => const TextStyle(fontSize: 14, color: Colors.white);
  TextStyle get bodyLarge => const TextStyle(fontSize: 16, color: Colors.white);
  TextStyle get titleLarge => const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white);
  TextStyle get labelMedium => const TextStyle(fontSize: 12, color: Colors.grey);
  TextStyle get headlineMedium => const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.white);

  Color get primary => Colors.blue;
  Color get secondary => Colors.purple;
  Color get alternate => Colors.amber;
  Color get primaryBackground => const Color(0xFF1A1A1A);
  Color get secondaryBackground => const Color(0xFF2A2A2A);
  Color get primaryText => Colors.white;
  Color get secondaryText => Colors.grey;
}
