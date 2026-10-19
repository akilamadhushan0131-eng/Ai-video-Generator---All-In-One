import 'package:flutter/material.dart';
import 'a_i_studio_dashboard_widget.dart';

// Auto-generated Mock Support for FlutterFlow Theme & Core Utilities
class FlutterFlowTheme {
  static FlutterFlowTheme of(BuildContext context) => FlutterFlowTheme();
  TextStyle get bodyMedium => const TextStyle(fontSize: 14, color: Colors.white);
  TextStyle get titleLarge => const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white);
  TextStyle get labelMedium => const TextStyle(fontSize: 12, color: Colors.grey);
  TextStyle get bodyLarge => const TextStyle(fontSize: 16, color: Colors.white);
  TextStyle get headlineMedium => const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.white);
  Color get primary => Colors.blue;
  Color get secondary => Colors.purple;
  Color get alternate => Colors.amber;
  Color get primaryBackground => const Color(0xFF1A1A1A);
  Color get secondaryBackground => const Color(0xFF2A2A2A);
  Color get primaryText => Colors.white;
  Color get secondaryText => Colors.grey;
}

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sinhala AI Studio',
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: const Color(0xFF1A1A1A),
      ),
      home: const AIStudioDashboardWidget(),
    );
  }
}
